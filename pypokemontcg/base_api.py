"""Basic setup for the other modules requests"""

from collections import namedtuple
import math

Result = namedtuple(
    'result', 
    [
        'json', 
        'status_code', 
        'page', 
        'page_size', 
        'total_count', 
        'pages',
        'has_next'
    ])


class BaseApi:
    """
    Base Class for all the api endpoints
    """
    
    def __init__(self, session, endpoint):
        self.endpoint = endpoint
        self.session = session
        self.base_url = "https://api.pokemontcg.io/v2/"
    
    def _get_result(self, url, params=None) -> Result:
        """
        Given a url, fetch the json result

        :param url: the Pokemon endpoint
        :param params: parameters for querystring

        :return: a namedtuple
        """
        response = self.session.get(url, params=params)
        
        if response.status_code == 200:
            json_response = response.json()
            pages = math.ceil(json_response['totalCount'] / json_response['pageSize'])
            output = Result(
                json_response['data'], 
                response.status_code, 
                json_response['page'], 
                json_response['pageSize'], 
                json_response['totalCount'],
                pages,
                True if json_response['page'] < pages else False
            )
        else:
            output = Result(
                None, 
                response.status_code, 
                None, 
                None, 
                None,
                None,
                None
            )
        
        return output

    def _set_params(self, page, page_size):
        return {
            'page': page,
            'pageSize': page_size
        }
    
    def all(self, page=1, page_size=250):
        f"""
        Download all {self.endpoint} data, with the maximum page size of 250

        :param page: page number
        :param page_size: size of the page. Max size is 250

        :return: namedtuple
        """
        self.count = page
        self.size = page_size
        params = self._set_params(self.count, self.size)
        return self._get_result(f'{self.base_url}{self.endpoint}', params=params)

    def next(self):
        """
        calls the next page based on the last method all() page 

        :return: namedtuple
        """
        self.count += 1
        return self.all(page=self.count, page_size=self.size)