from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import *


@api_view(['GET'])
def get_pokemon(request):
    pokemon = Pokemon.objects.count()
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

    serializer = PokemonSerializer(pokemon)

    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_poke_data(request):
    pokemon = Pokemon.objects.count()

    # serializer = PokemonSerializer(pokemon)

    return Response(pokemon, status=status.HTTP_200_OK)
