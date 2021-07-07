

from pypokemontcg.api_collections import base_api
from .base_api import BaseApi


class Cards(BaseApi):

    ENDPOINT = 'cards'
    PAGE_COUNT = None
    PAGE_SIZE = None

    def _set_params(self, page, page_size):
        return {
            'page': page,
            'pageSize': page_size
        }
    
    def all(self, page=1, page_size=250):
        self.PAGE_COUNT = page
        self.PAGE_SIZE = page_size
        params = self._set_params(self.PAGE_COUNT, self.PAGE_SIZE)
        return self.get_result(f'{self.base_url}{self.ENDPOINT}', params=params)
    
    def next(self):
        self.PAGE_COUNT += 1
        params = self._set_params(self.PAGE_COUNT, self.PAGE_SIZE)
        return self.get_result(f'{self.base_url}{self.ENDPOINT}', params=params)
    
    