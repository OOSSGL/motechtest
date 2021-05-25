# MOTech-Test Pokemon API
To use the API first install the requirements
- pip install -r requirements.txt

Then start the server
- python manage.py runserver

Then populate the DB by calling the POST service /pokemon/create_poke_data/
- http://127.0.0.1:8000/pokemon/create_poke_data/

It will populate the database with the data of all the Pokemon Chains available on pokeapi.co. It will take a few minutes.

And after that the API is ready to use with the service /pokemon/ by providing the name as query param
- http://127.0.0.1:8000/pokemon/?name=combusken

It will show the data of the pokemon and the evolutions related to the pokemon as intended

To run the test cases use the command pytest
- pytest

7 test cases were made, only 7 because of the short time available but it covers the most important cases

To see the documentation start the server an go to /redoc/
- http://127.0.0.1:8000/redoc/

Also added a class diagram of the models, it is the file class_diagram.png

Hope you enjoy it, despite the short time it was fun to do a project about Pokemon

Made by Oscar David Garcia Medina