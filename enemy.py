# Course: CS 30
# Period: 1
# Date: 21/04/30
# Name: William Teng
# Description: Enemy class


# The parent class
class Enemy():
    """Enemies with their name, health, and damage"""
    def __init__(self):
        raise NotImplementedError("Do not create raw enemy objects")

    def __str__(self):
        """The child class name is made into a string"""
        return self.name


# The child class with inherited properties from Enemy
class Guard(Enemy):
    """Guards the castle"""
    def __init__(self):
        # The name of the enemy
        self.name = "Guard"
        # The enemies health points
        self.hp = 30
        # The damage of the enemy
        self.damage = 10


# The child class with inherited properties from Enemy
class Servant(Enemy):
    """Serves the castle"""
    def __init__(self):
        # The name of the enemy
        self.name = "Servant"
        # The enemies health points
        self.hp = 35
        # The damage of the enemy
        self.damage = 5


# The child class with inherited properties from Enemy
class Knight(Enemy):
    """Patrols the castle"""
    def __init__(self):
        # The name of the enemy
        self.name = "Knight"
        # The enemies health points
        self.hp = 25
        # The damage of the enemy
        self.damage = 15
        
