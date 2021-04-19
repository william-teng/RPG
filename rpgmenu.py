# Course: CS 30
# Period: 1
# Date created: 21/04/18
# Date modified: 21/04/19
# Name: William Teng
# Description: RPG continuous game play

def available_actions(action):
  """Return a message to move in the desired direction."""
  return action.title()

print("Valid actions for current location")
print("\nGo in one of the following directions:")
print("* North\n* South\n* East\n* West")
print("Complete one of the following actions:")
print("* Explore\n* Attack\n* Defend\n* Drink potion\n* Quit")

while True:
  action = input("\nAction: ")
  if action.lower() == 'north':
    print("Go north!")
  elif action.lower() == 'south':
    print("Go south!")
  elif action.lower() == 'west':
    print("Go west!")
  elif action.lower() == 'east':
    print("Go east!")
  elif action.lower() == 'explore':
    print("Explore!")
  elif action.lower() == 'attack':
    print("Attack!")
  elif action.lower() == 'defend':
    print("Defend!")
  elif action.lower() == 'drink potion':
    print("Drink potion!")
  elif action.lower() == 'quit':
    break
  else:
    print("Invalid action!")
