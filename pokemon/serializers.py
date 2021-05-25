from rest_framework import serializers
from .models import Pokemon, Evolution


class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = '__all__'


class EvolutionsRelatedSerializer(serializers.Serializer):
    type = serializers.CharField(help_text='Type of evolution, can be Preevolution or Evolution')
    id = serializers.IntegerField(help_text='ID of the pokemon')
    name = serializers.CharField(help_text='Name of the pokemon')


class PokemonWithEvolutionsSerializer(serializers.Serializer):
    pokemon = PokemonSerializer(help_text='Data of the pokemon')
    evolutions_related = EvolutionsRelatedSerializer(
        help_text='Data of the related evolutions of this pokemon',
        many=True
    )


class CreatePokeDataResponseSerializer(serializers.Serializer):
    success = serializers.CharField(help_text='Message indicating the succes of the operation, and also '
                                              'indicating how many Pokemon were added to the database')
