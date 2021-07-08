from .base_api import BaseApi


class Cards(BaseApi):

    ENDPOINT = 'cards'
    count = None
    size = None

    def _set_params(self, page, page_size):
        return {
            'page': page,
            'pageSize': page_size
        }
    
    def all(self, page=1, page_size=250):
        self.count = page
        self.size = page_size
        params = self._set_params(self.count, self.size)
        return self.get_result(f'{self.base_url}{self.ENDPOINT}', params=params)

    def next(self):
        self.count += 1
        params = self._set_params(self.count, self.size)
        return self.get_result(f'{self.base_url}{self.ENDPOINT}', params=params)