#1a 
pokemon_list = ["Eevee", "Magikarp", "Jigglypuff", "Bulbasaur", "Mew"]
    #add item
pokemon_list.insert(2, "Gengar")
print (pokemon_list)
    #remove using value
pokemon_list.remove("Gengar")
print (pokemon_list)
    #remove using index
pokemon_list.pop(2)
print (pokemon_list)
    #print 3rd item in list
print (pokemon_list [3])
#1b
my_team = ["Landorus", "Weedle", "Spearow", "Pidgey", "Gardevoir"]
#1c
pokedex = pokemon_list + my_team
print (pokedex)
#1d
pokedex.insert(3, "Rattata")
print (pokedex)
#1e
pokedex_length = len(pokedex)
print (pokedex_length)
#1f
for item in pokedex:
    print (item)
#1g
if "Charizard" in pokedex:
    print ("Charizard is in the pokedex")