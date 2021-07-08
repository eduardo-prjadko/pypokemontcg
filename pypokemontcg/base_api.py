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
            page = json_response['page']
            page_size = json_response['pageSize']
            total_count = json_response['totalCount']
            pages = math.ceil(total_count / page_size)
            has_next = True if page < pages else False
        else:
            json_response = None
            page = None
            page_size = None
            total_count = None
            pages = None
            has_next = None
        
        output = Result(
            json_response['data'], 
            response.status_code, 
            page, 
            page_size, 
            total_count,
            pages,
            has_next)
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