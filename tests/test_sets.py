

def test_cards_all(pokemon_client):
    first_r = pokemon_client.sets.all()
    if first_r.has_next:
        second_r = pokemon_client.sets.next()
        assert second_r.status_code == 200
        assert second_r.page == 2
    assert first_r.has_next != None
    assert isinstance(first_r.pages, int) 
    assert first_r.status_code == 200
    assert first_r.page == 1
    

def test_last_has_next(pokemon_client):
    r = pokemon_client.sets.all()
    r = pokemon_client.sets.all(page=r.pages)
    assert r.has_next == False