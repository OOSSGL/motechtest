import pytest
from pokemon.utilities import *


@pytest.mark.django_db(transaction=True)
def test_success_get_charmander(client):
    call_evolution_chain(2)
    url = '/pokemon/?name=charmander'
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db(transaction=True)
def test_success_get_ditto(client):
    call_evolution_chain(66)
    url = '/pokemon/?name=ditto'
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db(transaction=True)
def test_success_get_torchic(client):
    call_evolution_chain(131)
    url = '/pokemon/?name=torchic'
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db(transaction=True)
def test_success_get_combusken_full_answer(client):
    call_evolution_chain(131)
    url = '/pokemon/?name=combusken'
    response = client.get(url)

    right_response = {
        "pokemon": {
            "id": 256,
            "name": "combusken",
            "height": 9.0,
            "weight": 195.0,
            "base_hp": 60.0,
            "base_attack": 85.0,
            "base_defense": 60.0,
            "base_special_attack": 85.0,
            "base_special_defense": 60.0,
            "base_speed": 55.0
        },
        "evolutions_related": [
            {
                "type": "Preevolution",
                "id": 255,
                "name": "torchic"
            },
            {
                "type": "Evolution",
                "id": 257,
                "name": "blaziken"
            }
        ]
    }

    assert response.status_code == 200
    assert response.data == right_response


@pytest.mark.django_db(transaction=True)
def test_error_404(client):
    call_evolution_chain(2)
    url = '/pokemon/?name=torchic'
    response = client.get(url)
    assert response.data == {'ERROR': "Pokemon with name 'torchic' was not found"}
    assert response.status_code == 404


@pytest.mark.django_db(transaction=True)
def test_error_400_no_param_name(client):
    call_evolution_chain(2)
    url = '/pokemon/'
    response = client.get(url)
    assert response.status_code == 400
    assert response.data == {'ERROR': 'Query param name is required.'}


@pytest.mark.django_db(transaction=True)
def test_error_400_param_name_empty(client):
    call_evolution_chain(2)
    url = '/pokemon/?name='
    response = client.get(url)
    assert response.status_code == 400
    assert response.data == {'ERROR': 'Query param name cannot be empty.'}

