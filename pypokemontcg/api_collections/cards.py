

from pypokemontcg.api_collections import base_api
from .base_api import BaseApi


class Cards(BaseApi):

    ENDPOINT = 'cards'

    def all(self):
        return self.get_result(f'{self.base_url}{self.ENDPOINT}')