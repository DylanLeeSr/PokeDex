from pokebase import pokemon

selectedMonster = "charmander"
monster = pokemon(selectedMonster)
print(f"{selectedMonster.capitalize()} height: {monster.height}")
print("ID:", monster.id)
print("Name:", monster.name)
print("Base Experience:", monster.base_experience)
print("Height:", monster.height)
print("Is Default:", monster.is_default)
print("Order:", monster.order)
print("Weight:", monster.weight)

ability_names = []
for ability_metadata in monster.abilities:
       ability_names.append(ability_metadata.ability)

print(f"{'Abilities:'} {', ' .join(map(str, ability_names))}")


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