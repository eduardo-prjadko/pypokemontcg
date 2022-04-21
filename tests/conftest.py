import os

import pytest

from pypokemontcg import PokemonTCG


@pytest.fixture
def pokemon_client():
    api_key = os.environ.get('API_KEY')
    client = PokemonTCG(api_key)
    return client