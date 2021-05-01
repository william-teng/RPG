# Course: CS 30
# Period: 1
# Date: 21/04/30
# Name: William Teng
# Description: Interactions with each room in the castle

from map import player
from enemy import *
from map_display import *


# The dungeon tile
def dungeon():
    while True:
        # A visual display of the map is printed
        print(map_display_4)
        print(map_display_5)
        print(map_display_6)
        # Lets the player know where they are
        print("\nYou are now in the dungeon. A knight is patrolling the area.")
        print("Type 'f' to fight or 'l' to go back to\
 the previous tile.")
        # Allows the player to input an action
        action = input("\nAction: ")
        if action == "f":
            player.fight(Knight())
        elif action == "l":
            break
        # An invalid command was used
        else:
            print("Invalid! Please try again.")


# The chapel tile
def chapel():
    while True:
       # A visual display of the map is printed
        print(map_display_10)
        print(map_display_11)
        print(map_display_12)
        # Lets the player know where they are
        print("\nYou are now in the chapel. A servant is roaming around.")
        print("Type 'f' to fight or 'l' to go back to\
 the previous tile.")
        # Allows the player to input an action
        action = input("Action: ")
        if action == "f":
            player.fight(Servant())
        elif action == "l":
            break
        # An invalid command was used
        else:
            print("Invalid! Please try again.")


# The armoury tile
def armoury():
    while True:
       # A visual display of the map is printed
        print(map_display_13)
        print(map_display_14)
        print(map_display_15)
        # Lets the player know where they are
        print("\nYou are now in the armoury. A guard is guarding the area.")
        print("Type 'f' to fight or 'l' to go back to\
 the previous tile.")
        # Allows the player to input an action
        action = input("Action: ")
        if action == "f":
            player.fight(Guard())
        elif action == "l":
            break
        # An invalid command was used
        else:
            print("Invalid! Please try again.")


# The kitchen tile
def kitchen():
    while True:
       # A visual display of the map is printed
        print(map_display_7)
        print(map_display_8)
        print(map_display_9)
        # Lets the player know where they are
        print("\nYou are now in the kitchen. No one is here.")
        print("You may rest here or leave. Type 'l' to go back to\
 the previous tile.")
        # Allows the player to input an action
        action = input("Action: ")
        if action == "l":
            break
        elif action == "q":
            break
        # An invalid command was used
        else:
            print("Invalid! Please try again.")


# The void tile
def void():
    while True:
      # Lets the player know where they are
      print("\nThis is the edge of the map, please return\
 to the previous tile.")
      # Allows the player to input an action
      action = input("Type 'l' to return to previous tile.")
      if action == "l":
        print("\nYou are back on the previous tile.")
        break
      elif action == "q":
        break
      # An invalid command was used
      else:
        print("Invalid! Please try again.")


# The finish tile
def finish():
    while True:
        print("\nYou have reached the end! Type 'w' to leave.")
        # Allows the player to input an action
        action = input("Action: ")
        if action == "w":
            quit()
        # An invalid command was used
        else:
            print("Invalid! Please try again.")
