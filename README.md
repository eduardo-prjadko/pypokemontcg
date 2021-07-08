# PyPokemonTCG (unofficial Pokemon TCG SDK release)

The present repo is an unofficial release of the [Pokemon TCG](https://pokemontcg.io/) SDK for python, for restricted purposes.

The main purpose of this package is to provide easy means to retrieve Pokemon TCG data for ETL processes or a datalake repository.

Since it's objective is restricted, this package doesn't cover all the API endpoints listed in the official Pokemon TCG Porject, but the two main endpoints to retrieve all the cards end sets lists.

In the following super fast documentation, you will find out how to retrieve these data using PyPokemonTCG.
<br><br>

# Official documentation of unofficial Pokemon TCG SDK

## Installing
```
pip install git+https://github.com/eduardo-prjadko/pypokemontcg.git
```

## Importing

```python
from pypokemontcg import PokemonTCG

pokeclient = PokemonTCG(<APP_KEY>)
```

## Retrieving data
```python
r = pokeclient.cards.all()

print(r.status_code)
print(r.json[0])
print(r.page)
print(r.page_size)
print(r.total_count)
print(r.pages)
print(r.has_next)
```

The terminal will show the following respose:
```console
$ 200
$ {'id': 'pl1-1', 'name': 'Ampharos', 'supertype': 'Pokémon', 'subtypes': ['Stage 2'], 'level': '57', 'hp': '130', 'types': ['Lightning'], 'evolvesFrom': 'Flaaffy', 'abilities': [{'name': 'Damage Bind', 'text': "Each Pokémon that has any damage counters on it (both yours and your opponent's) can't use any Poké-Powers.", 'type': 'Poké-Body'}], 'attacks': [{'name': 'Gigavolt', 'cost': ['Lightning', 'Colorless'], 'convertedEnergyCost': 2, 'damage': '30+', 'text': 'Flip a coin. If heads, this attack does 30 damage plus 30 more damage. If tails, the Defending Pokémon is now Paralyzed.'}, {'name': 'Reflect Energy', 'cost': ['Lightning', 'Colorless', 'Colorless'], 'convertedEnergyCost': 3, 'damage': '70', 'text': 'Move an Energy card attached to Ampharos to 1 of your Benched Pokémon.'}], 'weaknesses': [{'type': 'Fighting', 'value': '+30'}], 'resistances': [{'type': 'Metal', 'value': '-20'}], 'retreatCost': ['Colorless', 'Colorless'], 'convertedRetreatCost': 2, 'set': {'id': 'pl1', 'name': 'Platinum', 'series': 'Platinum', 'printedTotal': 127, 'total': 130, 'legalities': {'unlimited': 'Legal'}, 'ptcgoCode': 'PL', 'releaseDate': '2009/02/11', 'updatedAt': '2020/08/14 09:35:00', 'images': {'symbol': 'https://images.pokemontcg.io/pl1/symbol.png', 'logo': 'https://images.pokemontcg.io/pl1/logo.png'}}, 'number': '1', 'artist': 'Atsuko Nishida', 'rarity': 'Rare Holo', 'nationalPokedexNumbers': [181], 'legalities': {'unlimited': 'Legal'}, 'images': {'small': 'https://images.pokemontcg.io/pl1/1.png', 'large': 'https://images.pokemontcg.io/pl1/1_hires.png'}, 'tcgplayer': {'url': 'https://prices.pokemontcg.io/tcgplayer/pl1-1', 'updatedAt': '2021/07/07', 'prices': {'holofoil': {'low': 6.75, 'mid': 7.95, 'high': 10.99, 'market': 7.36, 'directLow': 7.0}, 'reverseHolofoil': {'low': 5.0, 'mid': 14.0, 'high': 14.98, 'market': 3.05, 'directLow': None}}}}
$ 1
$ 250
$ 13685
$ 55
$ True
```

To retrieve the next page you can use the `next()` method:
```python
while r.has_next:
    r = pokeclient.cards.next()
```
It's possible to retrieve specific page and specific page size by seting the repective parameters:
```python
r = pokeclient.cards.all(page=10, page_size=100)
```
All the same response structure and methods are available for retrieving sets:
```python
r = pokeclient.sets.all()
while r.has_next:
    r = pokeclient.sets.next()
```