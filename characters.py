# Playable characters in the RPG game
characters = {
  'john': {
    'race': 'human', 'health_points': '100'
    },

  'bob': {
    'race': 'goblin', 'health_points': '50'
    },

  'tim': {
    'race': 'orc', 'health_points': '150'
    },

  }

# Prints each character's information
for character, character_info in characters.items():
  print(f"\nCharacter: {character.title()}")
  race = character_info['race']
  health_points = character_info['health_points']

  print(f"{character.title()}'s race is {race}.")
  print(f"{character.title()} has {health_points} health points.")
