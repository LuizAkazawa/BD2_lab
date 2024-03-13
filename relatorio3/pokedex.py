from database import Database
from helper.writeAJson import writeAJson


class Pokedex:
    def __init__(self, Database: Database):
        _database = Database

    def grass_poison(self):
        db = Database(database="pokemons", collection="pokemons")
        tipos = ["Grass", "Poison"]
        pokemons = db.collection.find({"type": {"$in": tipos}})
        writeAJson(pokemons, "pokemons_grass-poison")

    def gte_80cm(self):
        db = Database(database="pokemons", collection="pokemons")
        pokemons = db.collection.find({"height": {"$gt": "0.80 m"}})
        writeAJson(pokemons, "pokemons_gte-80cm")

    def bug_poison(self):
        db = Database(database="pokemons", collection="pokemons")
        tipos = ["Bug", "Poison"]
        pokemons = db.collection.find({"type": {"$in": tipos}})
        writeAJson(pokemons, "pokemons_bug-poison")

    def gte_5kg(self):
        db = Database(database="pokemons", collection="pokemons")
        pokemons = db.collection.find({"weight" : {"$gt" : "5.0 kg"}})
        writeAJson(pokemons, "pokemons_gte-5kg")

    def spawnTime_gte_90s(self):
        db = Database(database="pokemons", collection="pokemons")
        pokemons = db.collection.find({"spawn_time" : {"$gt" : "01:30"}})
        writeAJson(pokemons, "pokemons_spawnTime-90s")
