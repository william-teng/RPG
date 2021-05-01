# Course: CS 30
# Period: 1
# Date: 21/04/30
# Name: William Teng
# Description: Player class

from random import randint


class Player:
    def __init__(self, x, y):
        # The player's health points
        self.hp = 100
        # The amount of damage the player can do
        self.dmg = 10

    def fight(self, g):
        enemy = g
        # While both health points are above 0, keep fighting
        while self.hp > 0 and enemy.hp > 0:
            # The enemy attacks
            enemy_attack = randint(1, 2)
            # Allows the player to attack
            action = input("\nType 'a' to attack: ")
            if action == "a":
                # Health points are deducted from enemy
                enemy.hp -= 10
                print(f"\nThe {enemy} has {enemy.hp} hp left.")
            else:
                # The player missed
                print("\nYou missed your attack!")
            # The enemy attack is 1 and hp is above zero
            if enemy_attack == 1 and enemy.hp > 0:
                # The player gets damaged
                self.hp -= enemy.damage
                print(f"The {enemy.name} attacks!\
 It deals {enemy.damage} damage!")
                # Prints how much hp the enemy has left
                if self.hp > 0:
                    print(f"\nYou have {self.hp} hp left.")
            # The enemy action is 2 and hp is above zero
            elif enemy_attack == 2 and enemy.hp > 0:
                print(f"The {enemy.name} missed their attack!")
        # Exits the game if the player dies
        if self.hp <= 0:
            print("\nYou are now dead.")
            exit()
        # The user has successfully killed the enemy
        else:
            print(f"\nYou have successfully defeated a {enemy}!")
