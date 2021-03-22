# A list of weapons
weapons = ['sword', 'bow', 'staff', 'crossbow', 'dagger']
print('Available weapons:')
for item, inv_item in enumerate(weapons, 1):
    print(f'{item}. {inv_item.title()}')

# A list of armour
armour = ['helmet', 'chestplate', 'pants', 'boots']
print('Available armour:')
for item, inv_item in enumerate(armour, 1):
    print(f'{item}. {inv_item.title()}')
