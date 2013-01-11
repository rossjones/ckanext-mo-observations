import logging


from ckanext.mo_observations.model import init_tables
from ckanext.mo_observations.lib.metoffice import MetOffice


from pylons import config
from ckan.lib.cli import CkanCommand


log = None

class UpdateData(CkanCommand):
    """

    """
    summary = __doc__.split('\n')[0]
    usage = __doc__
    max_args = 0
    min_args = 0

    def __init__(self, name):
        super(UpdateData, self).__init__(name)
        self.parser.add_option('-t', '--test',
                               action='store_true',
                               default=False,
                               dest='test',
                               help='Whether to use local test data instead of remote data')

    def command(self):
        import ckanclient
        from ckan.logic import get_action
        import urlparse, operator

        self._load_config()
        log = logging.getLogger("ckanext.mo_observations")

        import ckan.model as model
        model.Session.remove()
        model.Session.configure(bind=model.meta.engine)
        model.repo.new_revision()

        init_tables()
        log.info("Database initialised")

        key = config.get("datapoint.api_key")
        if not key:
            log.error("No API Key was found in config, please specify 'datapoint.api_key'")
            return

        mo = MetOffice(key, log)
        mo.process(self.options.test)
