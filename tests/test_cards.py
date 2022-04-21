import logging

from pypokemontcg import PokemonTCG


def test_cards_all(pokemon_client: PokemonTCG):
    first_r = pokemon_client.cards.all()

    logging.debug(f'Pokemon cards initiated with:')
    logging.debug(f'- {first_r.total_count} cards to retrieve.')
    logging.debug(f'- {first_r.pages} pages to inter.')

    if first_r.has_next:
        second_r = pokemon_client.cards.next()
    assert first_r.has_next != None
    assert isinstance(first_r.pages, int) 
    assert first_r.status_code == 200
    assert first_r.page == 1
    assert first_r.page_size == 250
    assert second_r.status_code == 200
    assert second_r.page == 2

def test_last_has_next(pokemon_client):
    r = pokemon_client.cards.all()
    r = pokemon_client.cards.all(page=r.pages)
    assert r.has_next == False