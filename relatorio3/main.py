from pokedex import Pokedex
from database import Database

db = Database(database="pokemons", collection="pokemons")

p = Pokedex(db)
p.grass_poison()
p.gte_80cm()
p.bug_poison()
p.gte_5kg()
p.spawnTime_gte_90s()

