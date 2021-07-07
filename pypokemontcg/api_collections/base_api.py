"""Basic setup for the other modules requests"""

from collections import namedtuple

Result = namedtuple('result', ['json', 'status_code'])


class BaseApi:
    """
    Base Class for all the other api_collections modules
    """

    def __init__(self, config):
        self.session = config.session
        self.base_url = "https://api.pokemontcg.io/v2/"
    
    def get_result(self, url) -> Result:
        """
        Given a url, fetch the json result

        :param url: the Pokemon endpoint
        :return: a namedtuple
        """
        response = self.session.get(url)
        if response.status_code == 200:
            json_response = response.json()
        else:
            json_response = None
        output = Result(json_response, response.status_code)
        return output