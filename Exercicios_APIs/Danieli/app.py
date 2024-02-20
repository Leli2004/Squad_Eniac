#########################
###### Desafio API ######
#########################

#importar flask:
from flask import Flask, render_template

import urllib.request, json

app = Flask(__name__)  #varíavel que trabalha com flask

@app.route("/")
def main():
    return render_template("index.html")

# Rota para chama o arquivo character.html
@app.route("/characters")
def lista_characters():
    url = "https://rickandmortyapi.com/api/character/"
    response = urllib.request.urlopen(url)
    data_c = response.read()
    dicionario = json.loads(data_c)

    return render_template("character.html", characters=dicionario["results"])

# Rota para chama o arquivo character-id.html
@app.route("/characters/<id>")
def lista_characters_id(id):
    url = "https://rickandmortyapi.com/api/character/" + id
    response = urllib.request.urlopen(url)
    data = response.read()
    dicio = json.loads(data)

    return render_template("character-id.html", charactersId=dicio)

# Rota para listar personagens em JSON
@app.route("/json_characters")
def lista_character_json():
    url = "https://rickandmortyapi.com/api/character/"
    response = urllib.request.urlopen(url)
    characters = response.read()
    charactersId = response.read()
    dicionario = json.loads(characters)
    dicio = json.loads(characters)

    characters = []
    charactersId = []

    for character in dicionario["results"]:
        character = {
            "id": character["id"],
            "name": character["name"],
            "image": character["image"],
            "status": character["status"],
            "species": character["species"],
            "gender": character["gender"],
            "origin": character["origin"],
            "location": character["location"],
            "episode": character["episode"]
        }
        characters.append(character)

    for characterId in dicio["results"]:
        characterId = {
            "id": characterId["id"],
            "name": characterId["name"],
            "image": characterId["image"],
            "status": characterId["status"],
            "species": characterId["species"],
            "gender": characterId["gender"],
            "origin": characterId["origin"],
            "location": characterId["location"],
            "episode": characterId["episode"]
        }
        charactersId.append(characterId)

    return {"characters": characters, "charactersId": charactersId}


# Rota para chama o arquivo episodes.html
@app.route("/episodes")
def lista_episodes():
    url = "https://rickandmortyapi.com/api/episode"
    response = urllib.request.urlopen(url)
    data_e = response.read()
    dicionario = json.loads(data_e)

    return render_template("episodes.html", episodes=dicionario["results"])

# Rota para chama o arquivo episodes-id.html
@app.route("/episodes/<id>")
def lista_episodes_id(id):
    url = "https://rickandmortyapi.com/api/episode/" + id
    response = urllib.request.urlopen(url)
    data = response.read()
    dicio = json.loads(data)

    return render_template("episode-id.html", episodesId=dicio)

# Rota para listar episodios em JSON
@app.route("/json_episodes")
def lista_episodes_json():
    url = "https://rickandmortyapi.com/api/episode"
    response = urllib.request.urlopen(url)
    episodes = response.read()
    episodesId = response.read()
    dicionario = json.loads(episodes)
    dicio = json.loads(episodes)

    episodes = []
    episodesId = []

    for episode in dicionario["results"]:
        episode = {
            "name": episode["name"],
            "air_date": episode["air_date"],
            "episode": episode["episode"]
        }
        episodes.append(episode)

    for episodeId in dicio["results"]:
        episodeId = {
            "name": episodeId["name"],
            "air_date": episodeId["air_date"],
            "episode": episodeId["episode"]
        }
        episodesId.append(episodeId)
    
    return {"episodes": episodes, "episodesId": episodesId}


# Rota para chama o arquivo locations.html
@app.route("/locations")
def lista_locations():
    url = "https://rickandmortyapi.com/api/location"
    response = urllib.request.urlopen(url)
    data_l = response.read()
    dicionario = json.loads(data_l)

    return render_template("locations.html", locations=dicionario["results"])

# Rota para chama o arquivo locations-id.html
@app.route("/locations/<id>")
def lista_location_id(id):
    url = "https://rickandmortyapi.com/api/location/" + id
    response = urllib.request.urlopen(url)
    data = response.read()
    dicio = json.loads(data)

    return render_template("locations-id.html", locationsId=dicio)

# Rota para listar localizações em JSON
@app.route("/json_locations")
def lista_locations_json():
    url = "https://rickandmortyapi.com/api/location"
    response = urllib.request.urlopen(url)
    locations = response.read()
    locationsId = response.read()
    dicionario = json.loads(locations)
    dicio = json.loads(locations)

    locations = []
    locationsId = []

    for location in dicionario["results"]:
        location = {
            "id": location["id"],
            "name": location["name"],
            "type": location["type"],
            "dimension": location["dimension"],
            "residents": location["residents"]
        }
        locations.append(location)

    for locationId in dicio["results"]:
        locationId = {
            "id": locationId["id"],
            "name": locationId["name"],
            "type": locationId["type"],
            "residents": locationId["residents"]
        }
        locationsId.append(locationId)

    return {"locations": locations, "locationsId": locationsId}