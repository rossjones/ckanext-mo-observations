import os
import json
import requests
import ckanext.mo_observations.model as mo_model

CAPS_URL = "http://datapoint.metoffice.gov.uk/public/data/val/wxobs/all/json/capabilities?res=hourly&key={key}"

class Capabilities(object):
    """
    """

    def __init__(self, api_key, log):
        self.log = log
        self.api_key = api_key
        super(Capabilities, self).__init__()

    def _test_data(self):
        self.log.debug("Loading capabilities test_data")
        f = os.path.abspath(os.path.join(os.path.abspath(__file__),
                                         os.pardir, os.pardir,
                                         "test_data/capabilities.json"))
        return json.load(open(f, "r"))


    def get(self, test=False):
        """
        """
        if not test:
            url = CAPS_URL.format(key=self.api_key)
            response = requests.get(url)
            if response.status_code != 200:
                self.log.error("Failed to retrieve capabilities from datapoint.")
            content = json.loads(response.content)
        else:
            content = self._test_data()

        return [ts for ts in content['Resource']['TimeSteps']['TS']]
