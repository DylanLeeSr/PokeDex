from pokebase import pokemon

selectedMonster = "charmander"
monster = pokemon(selectedMonster)
'''print(f"{selectedMonster.capitalize()} height: {monster.height}")
print("ID:", monster.id)
print("Name:", monster.name)
print("Base Experience:", monster.base_experience)
print("Height:", monster.height)
print("Is Default:", monster.is_default)
print("Order:", monster.order)
print("Weight:", monster.weight)'''
#print("Abilities:", monster.abilities)
#print(dir(monster.abilities[0])) used this to find what attributes in "APIMetadata" were used so i could target just "ability"
print("Abilities:")
for ability_metadata in monster.abilities:
    print(ability_metadata.ability)

'''print("Forms:", monster.forms)
print("Game Indices:", monster.game_indices)
print("Held Items:", monster.held_items)
print("Location Area Encounters:", monster.location_area_encounters)
print("Moves:", monster.moves)
print("Past Types:", monster.past_types)
print("Sprites:", monster.sprites)
print("Species:", monster.species)
print("Stats:", monster.stats)
print("Types:", monster.types)'''