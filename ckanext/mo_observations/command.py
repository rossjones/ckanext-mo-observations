import logging

from .model import init_tables
from pylons import config
from ckan.lib.cli import CkanCommand

# No other CKAN imports allowed until _load_config is run,
# or logging is disabled

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


