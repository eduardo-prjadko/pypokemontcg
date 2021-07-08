from .base_api import BaseApi


class Cards(BaseApi):
    """
    Class that holds all cards endpoint APIs
    """

    ENDPOINT = 'cards'
    count = None
    size = None

    def _set_params(self, page, page_size):
        return {
            'page': page,
            'pageSize': page_size
        }
    
    def all(self, page=1, page_size=250):
        """
        Download all cards data, with the maximum page size of 250

        :param page: page number
        :param page_size: size of the page. Max size is 250

        :return: namedtuple
        """
        self.count = page
        self.size = page_size
        params = self._set_params(self.count, self.size)
        return self.get_result(f'{self.base_url}{self.ENDPOINT}', params=params)

    def next(self):
        """
        calls the next page based on the last method all() page 

        :return: namedtuple
        """
        self.count += 1
        return self.all(page=self.count, page_size=self.size)