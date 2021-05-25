from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_pokemon, name='Get Pokemon'),
    path('create_poke_data/', views.create_poke_data, name='Create Poke Data'),
]
