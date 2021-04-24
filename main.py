# Course: CS 30
# Period: 1
# Date created: 21/04/18
# Date modified: 21/04/23
# Name: William Teng
# Description: RPG modules and maps

import random
from tabulate import tabulate


def append_list(dictionary, list):
  """Create a list from elements of a dictionary"""
  for x in dictionary:
    list.append(x)


def replace_tile(list, tile1, tile2):
  """Make sure that tiles do not overwrite each other"""
  while random_tile(list, tile1) == random_tile(list, tile2):
    random_tile(list, tile1)
    random_tile(list, tile2)


def random_tile(list, tile):
  """Choose a random tile to replace and return the indices"""
  x = random.choice(list)
  y = random.choice(x)
  n = list.index(x)
  m = x.index(y)
  list[n][m] = tile
  return (n, m)


def generate_map(list):
  """Randomly generate a 5x5 map from tile types"""
  map = [[random.choice(list) for i in range(5)] for j in range(5)]
  # add boss and start tiles
  replace_tile(map, "Big Boss", "Start")
  return map


def print_map(dictionary):
  """Print out each map generated"""
  for key in dictionary:
    map = dictionary[key]
    print(f"{key}")
    # format the maps in rows and columns
    print(tabulate(map, tablefmt="plain"))
    print ("\n")


# game locations
locations = {
  "Castle": "a fortified medieval building", "Fortress": "a stronghold"
  }

# map tile types
map_tiles = {
  "Enemy": {
    "description": "location of an enemy", "abbreviation": "ET", "action":
    "must defeat the enemy to continue"
    },

  "Big Boss": {
    "description": "Big Boss enemy location and the exit for the location",
    "abbreviation": "BT",
    "action": "may run away or fight the boss to continue"
    },

  "Weapons": {
    "description": "location of a weapon",
    "abbreviation": "WT",
    "action": "may pick up items or move to another location"
    },

  "Supplies": {
    "description": "location of protection and healing items",
    "abbreviation": "ST",
    "action": "must pick up the weapon to continue"
    },

  " ": {
    "description": "location with no items",
    "abbreviation": "BT",
    "action": "may rest or move to another location"
    },

  "Start": {
    "description": "entrance to the location",
    "abbreviation": "S",
    "action": "may rest or move to another location"
    },

  }

# generate a list of locations
location_level = []
append_list(locations, location_level)
# generate a list of tile types removing the start and boss tiles
tile_types = []
append_list(map_tiles, tile_types)
tile_types.remove("Big Boss")
tile_types.remove("Start")

# organize each city level and its map in a dictionary
main_map = {}
for location in location_level:
  location_map = generate_map(tile_types)
  main_map[location] = location_map

print_map(main_map)
