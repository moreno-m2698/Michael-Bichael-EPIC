import random
import json
import math
from Classes.actions import Items



class Unit:
    def __init__(self, name: str, atk: int, defense: int, maxHp: int, magic: int, level: int, agil: int):
        self.name = name
        self.atk = atk
        self.defense = defense
        self.maxHp = maxHp
        self.currentHp = self.maxHp
        self.magic = magic
        self.agil = agil
        self.status = "None"
        self.level = level
        

    def __str__(self):
        return f' {self.name}: Health:{self.currentHp}/{self.maxHp}' 

    
    def attack(self, target):
        # damage = 0

        # #ternary operator example
        
        # modifier = (critChance == 9) if 2 else 1
        
        # damage = self.atk * 100 / (100 + slime.defense) * modifier

        # # damage = self.atk * 100 / (100 + slime.defense) * ((critChance == 9) if 2 else 1)

        # hitString = (critChance == 9) if f"Slime got critically hit for {damage}." else f"Slime got hit for {damage}."

        # print(hitString)

        print(f'{self.name} attacked the {target.name} slime!')

        critChance = random.randint(1, 10)

        damage = 0
        if critChance == 9:
            print('It was a critical hit!')
            damage = int(self.atk * 100 / (100 + target.defense) * 2)
        else:
            damage = int(self.atk * 100 / (100 + target.defense))

        print(f'{self.name} did {damage} damage.')
        target.currentHp -= damage

        return target.currentHp
       


class Hero(Unit):
    #these are dunder functions __x___
    def __init__(self, name: str, atk: int, defense: int, maxHp: int, magic: int, level: int, agil: int):
        super().__init__(name, atk, defense, maxHp, magic, level, agil)
        self.healthpots = 5
        self.monstersKilled = 0
        self.currentExp= 0
        self.expNext = 0
        self.manaMax = manaMax
        self.manaCurrent = self.manaMax

    def levelUpCheck(self, monster):
        
        expEarn = monster(level) * monster(exp)

        self.currentExp += expEarn

        if self.expNext <= self.currentExp:
            
            self.currentExp -= self.expNext
            self.level += 1
            Hero.requiredExp(self)
            # Come back later to get this
        

    def __str__(self):
        return f'{super().__str__()} | {self.healthpots} potions'


    
    #Void function/None functions -> functions that dont have returns / dont give anything back / not expressions
    def potionUse(self):
        
        if self.healthpots > 0:
            
            if self.currentHp == self.maxHp:

                print(f'{self.name} is already full health!')
                return 0

            else:

                self.healthpots -= 1
                self.currentHp += 20

                if self.currentHp >= self.maxHp:
                    remainder = self.currentHp - self.maxHp
                    self.currentHp = self.maxHp
                    actual = 20 - remainder
                    print(f'{self.name} used a potion.\nHealed for {actual} HP.')
                    return 1
                    
                else:
                    print(f'{self.name} used a potion.\nHealed for 20 HP.')
                    return 1
        else:
            print(f'{self.name} has no potions!😭')
            return 0
    def passTurn(self):
        
        print(f'{self.name} passed.')

    def observe(self, slime):

        print(f'{self.name} looks intently at the {slime.type} slime.\n{slime.type} slime  has {slime.atk} attack and {slime.defense} defense.')

    def heroSelection(name):
        heroFile = open('JSON/hero.json')
        heroDict = json.load(heroFile)

        hero = heroDict[name]

        return Hero(name, hero['atk'], hero['defense'], hero['maxHp'])
    
    def findItem(self, amount):

        print(f'{self.name} found {amount} potion')

        self.healthpots += amount

    
class Slime(Unit):
    def __init__(self, atk: int, defense: int, maxHp: int, name: str):
        super().__init__(name, atk, defense, maxHp)
        self.isEpic = False
        

    def __str__(self):
        
        mainStr = super().__str__().split(':')

        return f'{mainStr[0]} Slime: {":".join(mainStr[1:])}'
        

    def attack(self, hero):
        print(f'The {self.name} Slime attacked {hero.name}!')

        critChance =  random.randint(1, 10)

        damage = 0
        if critChance == 9:
            print('It was a critical hit!')
            damage = int(self.atk * 100 / (100 + hero.defense) * 2)
        else:
            damage = int(self.atk * 100 / (100 + hero.defense))

        hero.currentHp -= damage

        print(f'It did {damage} damage!')

        return hero.currentHp

    def potionDrop(self, hero):

        if self.type != 'Treasure':
            if random.randint(1,6) == 1:
                hero.findItem(1)


        else:
            hero.findItem(2)

    def generateSlime():

        slimeTypeList = ['Green', 'Red', 'Blue', 'Yellow', "Black", 'Pink', 'Purple', 'White', 'Treasure']
        slimeAtkRdn = random.randint(7,12)
        slimeDefRdn = random.randint(7,12)
        slimeHpRdn = random.randint(40,60)

        return Slime(slimeAtkRdn, slimeDefRdn, slimeHpRdn, random.choice(slimeTypeList))

    # {'atk': 4, 'defense': 3, 'maxHp': 10, 'currentHp': 10, 'type': 'Green', 'epic': True}
    #      hero = {}
    #      hero["HP"] = 10
    #      hero["Name"] = "Jonathan Stewart The Third Hero of Plebs"
    #      hero["Atk"] = 9
    def generateSlimeJSON():
        slimeFile = open('slime.json')
        slimeList = json.load(slimeFile)

        slime = slimeList[0]


        return Slime(slime['atk'], slime['defense'], slime['maxHp'], slime['currentHp'], slime['type'])


