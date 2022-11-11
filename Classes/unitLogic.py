import random
import json
import math
from Classes.actions import Items
from monsterLogic import Monster



class Unit:
    def __init__(self, name: str,subClass: str, atk: int, defense: int, maxHp: int, magic: int, level: int, agil: int, luck: int):
        self.name = name
        self.subClass = subClass
        self.atk = atk
        self.defense = defense
        self.maxHp = maxHp
        self.currentHp = self.maxHp
        self.magic = magic
        self.agil = agil
        self.status = "None"
        self.level = level
        self.luck = luck
        self.trueName = self.name
    def monsterCheeck(self):
        if type(self) == Monster:
            self.trueName = f'{self.subClass} {self.name}'

    def __str__(self):
        return f' {self.trueName}: Health:{self.currentHp}/{self.maxHp}' 

    def dodge(self):
        success = 1 == random.randint(1, 100 -  (2 * self.agil) - self.luck)
        return success

    
    def attack(self, target):
        # damage = 0
        # #ternary operator example
        # modifier = (critChance == 9) if 2 else 1
        # damage = self.atk * 100 / (100 + slime.defense) * modifier
        # # damage = self.atk * 100 / (100 + slime.defense) * ((critChance == 9) if 2 else 1)
        # hitString = (critChance == 9) if f"Slime got critically hit for {damage}." else f"Slime got hit for {damage}."
        # print(hitString)

        print(f'{self.name} attacked the {target.name} slime!')

        if Unit.dodge(target):
            print(f'{target.name} dodged the attack!')
            
        else:
            critChance = random.randint(1, 50 - (2 * self.luck) - self.agil)
            damage = 0
            if critChance == 1:
                print('It was a critical hit!')
                damage = int(self.atk * 100 / (100 + target.defense) * 2)
            else:
                damage = int(self.atk * 100 / (100 + target.defense))

            print(f'{self.name} did {damage} damage.')
            target.currentHp -= damage

            return target.currentHp

    def generateMonsterJSON():
        monsterFile = open('JSON/monsterList.json')
        monsterSelect = json.load(monsterFile)

        slime = monsterSelect[0]


        return Monster(slime['atk'], slime['defense'], slime['maxHp'], slime['currentHp'], slime['type'])
       

    # come back and work on how to spawn in units later


