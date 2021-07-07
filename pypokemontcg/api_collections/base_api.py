"""Basic setup for the other modules requests"""

from collections import namedtuple

Result = namedtuple('result', ['json', 'status_code', 'page'])


class BaseApi:
    """
    Base Class for all the other api_collections modules
    """

    def __init__(self, config):
        self.session = config.session
        self.base_url = "https://api.pokemontcg.io/v2/"
    
    def get_result(self, url, params=None) -> Result:
        """
        Given a url, fetch the json result

        :param url: the Pokemon endpoint
        :param params: parameters for querystring

        :return: a namedtuple
        """
        response = self.session.get(url, params=params)
        
        if response.status_code == 200:
            json_response = response.json()
            page = json_response['page']
        else:
            json_response = None
            page = None
        output = Result(json_response, response.status_code, page)
        return output