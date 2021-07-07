"""Basic setup for the other modules requests"""

from collections import namedtuple
import math

Result = namedtuple('result', ['json', 'status_code', 'page', 'page_size', 'total_count'])


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
            page_size = json_response['pageSize']
            total_count = json_response['totalCount']
            pages = math.ceil(total_count / page_size)
        else:
            json_response = None
            page = None
            page_size = None
            total_count = None
        output = Result(json_response, response.status_code, page, page_size, total_count)
        return output