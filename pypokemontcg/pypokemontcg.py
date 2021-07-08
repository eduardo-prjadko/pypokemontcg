"""
Code for the PokemonTCG class, that wraps the APIs into a single client object.
Each pokemon microservice have its dedicate module inside the api_collections package
"""
import requests

from .base_api import BaseApi


class PokemonTCG:
    """
    Client class for the Pokemon apis endpoints
    """

    def __init__(self, api_key=None, session=None):
        """
        Setup the parameters values and create attributes composing with the api_collections modules

        :param api_key: Your Pokemon api_key
        :param session: a requests Session object, to reuse the TCP connection
        """
        self.api_key = api_key
        self.session = self._init_session(session)

        self.cards = BaseApi(session=self.session, endpoint='cards')
        self.sets = BaseApi(session=self.session, endpoint='sets')

    def _get_header(self):
        """
        Setup the request header

        :return: dict()
        """
        return {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'X-Api-Key': self.api_key
        }
    
    def _init_session(self, session):
        """
        Initialize the session and its header

        :param session:
        :return: a requests Session object
        """
        if not session:
            session = requests.Session()

        headers = self._get_header()
        session.headers.update(headers)
        return session