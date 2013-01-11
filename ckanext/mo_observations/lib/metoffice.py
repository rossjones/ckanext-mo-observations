import datetime
import dateutil.parser
import ckanext.mo_observations.model as mo_model

from ckanext.mo_observations.lib.capabilities import Capabilities

class MetOffice(object):
    """
    """

    def __init__(self, api_key, log):
        self.log = log
        self.apikey = api_key
        super(MetOffice, self).__init__()

    def process(self, test=False):
        """
        """
        cap = Capabilities(self.apikey, self.log)
        caps = cap.get(test)

        for c in caps:
            when = dateutil.parser.parse(c)
            if mo_model.TimeStep.find(when):
                self.log.info("We already have this timestep")
            else:
                self.get_data(when)

    def get_data(self, timestamp):
        self.log.info("Getting data for %r" % timestamp)
        # Fetch the data, and parse it.
        # Once we have the data, we can create the TimeStep and Observation
        # objects to be saved. Ideally in a transaction.



