import random
import json
import math
from Classes.actions import Items
from Classes.playerLogic import Hero
from Classes.monsterLogic import Monster

def encounter():
    
    monster1 = Monster.generateMonsterJSON()
    monster2 = Monster.generateMonsterJSON()
    print(f'You see a {monster1} and a {monster2} in the distance.\n Which one do you choice to fight?')
    
    while True:
        choice = input(f"Fight 1. {monster1.name} or 2. {monster2.name}?\n")
        if choice == '1':
            return monster1
        elif choice == '2':
            return monster2
        else:
            print('Please give a valid value')
        
