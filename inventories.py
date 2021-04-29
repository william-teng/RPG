# Course: CS 30
# Period: 1
# Date created: 21/04/28
# Date modified: 21/04/28
# Name: William Teng
# Description: RPG classes

class Inventory():
  """The inventory of each character"""
  def __init__(self, name, weapon, shield, damage, protection):
    """Initialize name, weapon, shield, damage, and protection"""
    self.name = name
    self.weapon = weapon
    self.shield = shield
    self.damage = damage
    self.protection = protection

  def __str__(self):
    description = f"""
The {self.weapon} can only be used by {self.name}.
The {self.shield} has a protection value of {self.protection}.
The {self.weapon} has an attack value of {self.damage}.
    """
    return description


def character_inventory(inventories):
  """print a list of inventories"""
  for inventory in inventories:
    print(inventory)


def character_inventories(name):
  """checks which inventory belongs to which character"""
  if name == 'John':
    print(john_inventory)
  elif name == 'Bob':
    print(bob_inventory)
  elif name == 'Tim':
    print(tim_inventory)

# define each character's inventory and characteristics
john_inventory = Inventory("john", "sword", "shield", 50, 50)
bob_inventory = Inventory("bob", "dagger", "shield", 100, 0)
tim_inventory = Inventory("tim", "mace", "shield", 75, 0)

inventories = [john_inventory, bob_inventory, tim_inventory]

character_inventory(inventories)
