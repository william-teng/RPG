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

# John's inventory
# Includes a sword and a healing potion
john_inventory = {
  'sword': {
    'description': 'a long metal blade', 'damage': '50', 'protection': '50'
    },

  'healing potion': {
    'description': 'heals 50 health points', 'damage': '0', 'protection': '0'
  },

  }

# Lists John's inventory
print("\nJohn's Inventory:")

# Prints John's inventory and it's description
for item, item_info in john_inventory.items():
  print(f"* {item.title()}")
  description = item_info['description']
  damage = item_info['damage']
  protection = item_info['protection']

  print(f"\tdescription: {description}")
  print(f"\tdamage: {damage}")
  print(f"\tprotection: {protection}")

# Bob's inventory
# Includes a dagger and a stealth potion
bob_inventory = {
  'dagger': {
    'description': 'a short edged knife', 'damage': '100', 'protection': '0'
    },

  'stealth potion': {
    'description': 'increases chance to evade enemy',
    'damage': '0', 'protection': '0'
    },

  }

# Lists Bob's inventory
print("\nBob's Inventory:")

# Print's Bob's inventory and it's description
for item, item_info in bob_inventory.items():
  print(f"* {item.title()}")
  description = item_info['description']
  damage = item_info['damage']
  protection = item_info['protection']

  print(f"\tdescription: {description}")
  print(f"\tdamage: {damage}")
  print(f"\tprotection: {protection}")

# Tim's inventory
# Includes a mace and a strength potion
tim_inventory = {
  'mace': {
    'description': 'a club with spikes', 'damage': '75', 'protection': '25'
    },

  'strength potion': {
    'description': 'gain 25 strength points', 'damage': '0', 'protection': '0'
    },

  }

# Lists Tim's inventory
print("\nTim's Inventory:")

# Prints Tim's inventory and it's description
for item, item_info in tim_inventory.items():
  print(f"* {item.title()}")
  description = item_info['description']
  damage = item_info['damage']
  protection = item_info['protection']

  print(f"\tdescription: {description}")
  print(f"\tdamage: {damage}")
  print(f"\tprotection: {protection}")

# Locations in the RPG game
locations = {
  'enemy tile': {
    'description': 'This is a location of an enemy. '
    'You must defeat the enemy to continue'
    },

  'boss tile': {
    'description': 'This is a location of a Big Boss enemy. '
    'You may run away or fight the boss to continue'
    },

  'weapons tile': {
    'description': 'This is a location of a weapon. '
    'You may pick up the item or move to another location'
    },

  'supply tile': {
    'description': 'This is a location of potion and protection items. '
    'You may pick up the item or move to another location'
    },

  'blank tile': {
    'description': 'This is a location with no items. '
    'You may rest or move to another location'
    },

  }

# Prints each location and it's description
for location, description in locations.items():
  description = description['description']
  print(f"\nYou are on a {location.title()}. {description}.")
