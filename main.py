# Course: CS 30
# Period: 1
# Date: 21/04/30
# Name: William Teng
# Description: RPG Game

import random
from tabulate import tabulate
import map
from map import *
from map_display import *
from player import Player
import room

# Introduction message
print("Welcome to Castle Adventure!\n")
# Prints a visual map for the user to see
print("CASTLE MAP:")
print(map_display_1)
print(map_display_2)
print(map_display_3)


def area():
    global castle
    """Player is able to move around the map"""
    while True:
        # Instructions on the game
        print("\nINSTRUCTIONS:")
        print("* Your objective is to move to the 'end' tile.")
        print("* You are 'PLAYER', as shown on the map.")
        print("* You will encounter enemies as you move.")
        print("* If you recieve no message, it means\
 you are on an empty tile.")
        print("* Be cautious and do not leave the map area.")
        print("* Type 'q' if you wish to quit.")
        print("\nType to move in the following: up, right, down, left")
        # The player can input actions in four directions
        user = input('Action: ')
        user = user.lower()
        # The player is trying to go up
        if user == 'up':
            # Locates player in the castle
            for y, row in enumerate(map.castle):
                for x, object in enumerate(row):
                    if isinstance(object, Player):
                        if isinstance(map.castle[y - 1][x], armoury):
                            room.armoury()
                        elif isinstance(map.castle[y - 1][x], void):
                            room.void()
                        elif isinstance(map.castle[y - 1][x], kitchen):
                            room.kitchen()
                        elif isinstance(map.castle[y - 1][x], dungeon):
                            room.dungeon()
                        elif isinstance(map.castle[y - 1][x], chapel):
                            room.chapel()
                        elif isinstance(map.castle[y - 1][x], finish):
                            room.finish()
                        else:
                            # The player goes up
                            map.castle[y - 1][x] = object
                            # None tile is replaced
                            map.castle[y][x] = None
                            area()
                            # Returns the new position
                            return
        # The player is trying to go right
        elif user == 'right':
            # Locates player in the castle
            for y, row in enumerate(map.castle):
                for x, object in enumerate(row):
                    if isinstance(object, Player):
                        if isinstance(map.castle[y][x + 1], armoury):
                            room.armoury()
                        elif isinstance(map.castle[y][x + 1], void):
                            room.void()
                        elif isinstance(map.castle[y][x + 1], kitchen):
                            room.kitchen()
                        elif isinstance(map.castle[y][x + 1], dungeon):
                            room.dungeon()
                        elif isinstance(map.castle[y][x + 1], chapel):
                            room.chapel()
                        elif isinstance(map.castle[y][x + 1], finish):
                            room.finish()
                        else:
                            # The player goes right
                            map.castle[y][x + 1] = object
                            # None tile is replaced
                            map.castle[y][x] = None
                            area()
                            # Returns the new position
                            return
        # The player is trying to go down
        elif user == 'down':
            # Locates player in the castle
            for y, row in enumerate(map.castle):
                for x, object in enumerate(row):
                    if isinstance(object, Player):
                        if isinstance(map.castle[y + 1][x], armoury):
                            room.armoury()
                        elif isinstance(map.castle[y + 1][x], void):
                            room.void()
                        elif isinstance(map.castle[y + 1][x], kitchen):
                            room.kitchen()
                        elif isinstance(map.castle[y + 1][x], dungeon):
                            room.dungeon()
                        elif isinstance(map.castle[y + 1][x], chapel):
                            room.chapel()
                        elif isinstance(map.castle[y + 1][x], finish):
                            room.finish()
                        else:
                            # The player goes down
                            map.castle[y + 1][x] = object
                            # None tile is replaced
                            map.castle[y][x] = None
                            area()
                            # Returns the new position
                            return
        # The player is trying to go left
        elif user == 'left':
            # Locates player in the castle
            for y, row in enumerate(map.castle):
                for x, object in enumerate(row):
                    if isinstance(object, Player):
                        if isinstance(map.castle[y][x - 1], armoury):
                            room.armoury()
                        elif isinstance(map.castle[y][x - 1], void):
                            room.void()
                        elif isinstance(map.castle[y][x - 1], kitchen):
                            room.kitchen()
                        elif isinstance(map.castle[y][x - 1], dungeon):
                            room.dungeon()
                        elif isinstance(map.castle[y][x - 1], chapel):
                            room.chapel()
                        elif isinstance(map.castle[y][x - 1], finish):
                            room.finish()
                        else:
                            # The player goes left
                            map.castle[y][x - 1] = object
                            # None tile is replaced
                            map.castle[y][x] = None
                            area()
                            # Returns the new position
                            return
        # The player types q to quit
        elif user == 'q':
            break
        else:
            # An invalid command was used
            print('Invalid! Please try again.')

area()
