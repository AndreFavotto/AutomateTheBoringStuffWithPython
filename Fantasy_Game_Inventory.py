#this code simulates a fantasy game's inventory menu, where you can view, add or remove things from your inventory
import sys

stuff = {'ropes': 1, 'torches': 6, 'gold coins': 42, 'daggers': 1, 'arrows': 12}

def displayInventory(inventory):
    print("Current Inventory:")
    item_total=0
    for k, v in inventory.items():
        print(v, k)
        item_total += v
    print (f'Total of items:{item_total}\n')
    main()

def addItems(inventory):
    item = input('Which item do you want to add? Remember to type it in the plural form.\n').lower()
    if item in inventory:
        add = int(input(f'How many {item} do you want to add? '))
        inventory[item] += add
        print(f'{add} {item} successfully added to your inventory!\n')
        main()
    else:
        add = int(input(f'You have no {item} in your inventory! How many {item} do you want to add? '))
        inventory.setdefault(item, add)
        print(f'{add} {item} successfully added to your inventory!\n')
        main()

def removeItems(inventory):
    item = input('Which item do you want to remove? Remember to type it in the plural form.\n').lower()
    if item in inventory:
        rem = int(input(f'How many {item} do you want to remove? '))
        inventory[item] -= rem
        if inventory[item] <= 0:
            del inventory[f'{item}']
        print(f'{rem} {item} successfully removed from your inventory!\n')
    else:
        print(f"There's no {item} in your inventory!")
    main()

def main():
    op = int(input('What do you want to do?\n1 - View my inventory\n2 - Add items to my inventory\n3 - Remove items from my inventory\n4 - Exit\n'))
    if op == 1:
        displayInventory(stuff)
    elif op == 2:
        addItems(stuff)
    elif op == 3:
        removeItems(stuff)
    elif op == 4:
        sys.exit()
    else:
        print('Invalid option!')
        main()
main()