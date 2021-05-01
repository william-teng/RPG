# Course: CS 30
# Period: 1
# Date: 21/04/30
# Name: William Teng
# Description: Map

from player import Player

player = Player(1, 2)


# The parent class
class Tile:
    """Default tile for the map"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        """The child class name is made into a string"""
        return self.name


# The child class with inherited properties from Tile
class dungeon(Tile):
    """A strong underground prison cell"""
    def __init__(self, x, y):
        self.name = "dungeon"
        super().__init__(x, y)


# The child class with inherited properties from Tile
class chapel(Tile):
    """A room for Christian worship"""
    def __init__(self, x, y):
        self.name = "chapel"
        super().__init__(x, y)


# The child class with inherited properties from Tile
class kitchen(Tile):
    """A room where food is prepared and cooked"""
    def __init__(self, x, y):
        self.name = "kitchen"
        super().__init__(x, y)


# The child class with inherited properties from Tile
class armoury(Tile):
    """A place where weapons are kept"""
    def __init__(self, x, y):
        self.name = "armoury"
        super().__init__(x, y)


# The child class with inherited properties from Tile
class void(Tile):
    """A wall that prevents the player from leaving the map"""
    def __init__(self, x, y):
        self.name = "void"
        super().__init__(x, y)


# The child class with inherited properties from Tile
class finish(Tile):
    """The victory tile"""
    def __init__(self, x, y):
        self.name = "finish"
        super().__init__(x, y)

# Various rooms in the castle and their location
castle = [[void(0, 0), void(1, 0), void(2, 0), void(3, 0), void(4, 0)],
          [void(0, 1), dungeon(1, 1), kitchen(2, 1), chapel(3, 1), void(4, 1)],
          [void(0, 2), None, None, None, void(4, 2)],
          [void(0, 3), Player(1, 3), armoury(2, 3), finish(3, 3), void(4, 3)],
          [void(0, 4), void(1, 4), void(2, 4), void(3, 4), void(4, 4)]]
