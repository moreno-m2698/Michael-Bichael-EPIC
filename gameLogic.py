import random
import json
import math
from Classes.actions import Items
from Classes.playerLogic import Hero
from Classes.monsterLogic import Monster

def encounter():
    fileInUse = 'JSON/slime.json'
    monster1 = Monster.generateMonsterJSON(fileInUse)
    monster2 = Monster.generateMonsterJSON(fileInUse)
    while monster1.name == monster2.name:
        monster2 = Monster.generateMonsterJSON(fileInUse)

    print(f'You see a {monster1.name} and a {monster2.name} in the distance.\nWhich one do you choice to fight?')
    


    while True:
        choice = input(f"Fight 1. {monster1.name} or 2. {monster2.name}?\n")
        if choice == '1':
            return monster1
        elif choice == '2':
            return monster2
        else:
            print('Please give a valid value')

def rewards(hero, monster):
        #This caused an issue:

        #Logic behind it, make a list so that we can scan the dictionary keys but then call for the values of the keys using the dictionary and not the newly created list
        dropsList = list(monster.drops)
        print(hero.inventory)
        for id in dropsList:
            realItems = Items.itemSpawn(id,hero)
            counter = 0
            success = 0
            while counter < monster.drops[id]['cycles']:
                if 1 == monster.drops[id]['chance']:
                    if realItems in hero.inventory:
                        hero.inventory[realItems] += 1
                        
                    else:
                        hero.inventory[realItems] = 1
                    success += 1
                counter += 1
            if success != 0 and success == 1:
                # Come back and find out how to reformat the brackets
                print({f'Found {success} {realItems.name}!'})

            elif success != 0 and success > 1:
                print({f'Found {success} {realItems.name}s!'})                
        
