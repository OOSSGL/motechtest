from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import *
from .utilities import *


@api_view(['GET'])
def get_pokemon(request):
    if 'name' not in request.query_params:
        data = {'ERROR': 'Query param name is required.'}
        return Response(data, status=status.HTTP_400_BAD_REQUEST)
    if not request.query_params['name']:
        data = {'ERROR': 'Query param name cannot be empty.'}
        return Response(data, status=status.HTTP_400_BAD_REQUEST)

    name = request.query_params['name']

    pokemon = Pokemon.objects.filter(name=name.lower()).first()

    if not pokemon:
        data = {'ERROR': "Pokemon with name '" + str(name) + "' was not found"}
        return Response(data, status=status.HTTP_404_NOT_FOUND)

    # Get preevolutions and evolutions
    poke_evos = []

    pre_evos = Evolution.objects.filter(evolution=pokemon)
    for pre_evo in pre_evos:
        add_pre_evo = {
            'type': 'Preevolution',
            'id': pre_evo.preevolution.pk,
            'name': pre_evo.preevolution.name
        }
        poke_evos.append(add_pre_evo)

    evos = Evolution.objects.filter(preevolution=pokemon)
    for evo in evos:
        add_evo = {
            'type': 'Evolution',
            'id': evo.evolution.pk,
            'name': evo.evolution.name
        }
        poke_evos.append(add_evo)

    data = {
        'pokemon': pokemon,
        'evolutions_related': poke_evos
    }

    serializer = PokemonWithEvolutionsSerializer(data)

    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_poke_data(request):
    pokemon_added = Pokemon.objects.count()

    create_pokemon_data()

    pokemon_added = Pokemon.objects.count() - pokemon_added

    data = {
        'success': 'Pokemon added: ' + str(pokemon_added)
    }

    return Response(data, status=status.HTTP_200_OK)
