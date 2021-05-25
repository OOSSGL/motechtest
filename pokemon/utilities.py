import requests
from .models import Pokemon, Evolution


def add_poke_by_pokemon_species(pokemon_species_url):
    response = requests.get(pokemon_species_url)
    pokemon_species = response.json()

    # Check if already exists, if yes skip pokemon
    old_poke = Pokemon.objects.filter(pk=pokemon_species['id']).first()
    if old_poke:
        return True

    new_poke = Pokemon()
    new_poke.pk = pokemon_species['id']
    new_poke.name = pokemon_species['name']
    new_poke.save()

    # Add evolutions
    if pokemon_species['evolves_from_species']:
        evolution = Evolution()
        preev_poke = Pokemon.objects.filter(
            name=pokemon_species['evolves_from_species']['name']
        ).first()

        evolution.preevolution = preev_poke
        evolution.evolution = new_poke
        evolution.save()

    response = requests.get('https://pokeapi.co/api/v2/pokemon/{}/'.format(new_poke.pk))
    pokemon = response.json()

    new_poke.height = pokemon['height']
    new_poke.weight = pokemon['weight']

    for stat in pokemon['stats']:
        if stat['stat']['name'] == 'hp':
            new_poke.base_hp = stat['base_stat']
            continue
        if stat['stat']['name'] == 'attack':
            new_poke.base_attack = stat['base_stat']
            continue
        if stat['stat']['name'] == 'defense':
            new_poke.base_defense = stat['base_stat']
            continue
        if stat['stat']['name'] == 'special-attack':
            new_poke.base_special_attack = stat['base_stat']
            continue
        if stat['stat']['name'] == 'special-defense':
            new_poke.base_special_defense = stat['base_stat']
            continue
        if stat['stat']['name'] == 'speed':
            new_poke.base_speed = stat['base_stat']
            continue

    new_poke.save()
    print('Pokemon added: ', new_poke.name)

    return True


def call_evolutions(chain):
    for evolution in chain:
        add_poke_by_pokemon_species(evolution['species']['url'])

        # If it has another evolution we call the method again, until it finds no more evolutions
        if evolution['evolves_to']:
            print('Entered recursive function for pokemon: ', evolution['species']['name'])
            call_evolutions(evolution['evolves_to'])

    return True


def call_evolution_chain(chain_id):
    response = requests.get('https://pokeapi.co/api/v2/evolution-chain/{}/'.format(chain_id))
    if not response:
        return False
    chain = response.json()

    add_poke_by_pokemon_species(chain['chain']['species']['url'])

    if chain['chain']['evolves_to']:
        call_evolutions(chain['chain']['evolves_to'])

    return True


def create_pokemon_data():
    for i in range(1, 500):
        call_evolution_chain(i)
    return True
