from . import pokemon_client


def test_cards_all(pokemon_client):
    r = pokemon_client.cards.all()
    assert r.status_code == 200