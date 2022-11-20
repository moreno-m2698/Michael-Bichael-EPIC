import random
import math
from Classes.unitLogic import Unit
import json
from Classes.actions import Item



class Hero(Unit):
    #these are dunder functions __x___
    def __init__(self, name: str, atk: int, defense: int, maxHp: int, magic: int, level: int, agil: int, luck: int, manaMax:int):
        super().__init__(name, atk, defense, maxHp, magic, level, agil, luck)
        self.monstersKilled = 0
        self.currentExp= 0
        self.expNext = 0
        self.manaMax = manaMax
        self.manaCurrent = self.manaMax
        self.inventory = {}
        

    def levelUpCheck(self, monster):
        
        expEarn = monster(level) * monster(exp)

        self.currentExp += expEarn

        if self.expNext <= self.currentExp:
            
            self.currentExp -= self.expNext
            self.level += 1
            Hero.requiredExp(self)
            # Come back later to get this
        
    def __str__(self):
        return f'{super().__str__()} | {self.manaCurrent} / {self.manaMax}'
    
    #Void function/None functions -> functions that dont have returns / dont give anything back / not expressions
    
    def passTurn(self):
        
        print(f'{self.name} passed.')

    def observe(self, monster):

        print(f'{self.name} looks intently at the {monster.type} slime.\n{monster.type} slime  has {monster.atk} attack and {monster.defense} defense.')

    def heroSelection(name):
        heroFile = open('JSON/hero.json')
        heroDict = json.load(heroFile)

        hero = heroDict[name]

        return Hero(name, hero['atk'], hero['defense'], hero['maxHp'],hero['magic'], hero['level'], hero['agil'], hero['luck'], hero['maxMana'])
    
    def giveItem(self, item, amount):

        if amount != 1:
            print(f'{self.name} found {amount} {item}s!')

        else:
            print(f'{self.name} found ')


    def inventoryAccess(self):
        i = 1
        for keys in self.inventory:

            print(f'{i}. {keys.name} {keys.description} | {self.inventory[keys]}')
            i += 1
            
        return i








                

        





# def potionUse(self):
        
#         if self.healthpots > 0:
            
#             if self.currentHp == self.maxHp:

#                 print(f'{self.name} is already full health!')
#                 return 0

#             else:

#                 self.healthpots -= 1
#                 self.currentHp += 20

#                 if self.currentHp >= self.maxHp:
#                     remainder = self.currentHp - self.maxHp
#                     self.currentHp = self.maxHp
#                     actual = 20 - remainder
#                     print(f'{self.name} used a potion.\nHealed for {actual} HP.')
#                     return 1
                    
#                 else:
#                     print(f'{self.name} used a potion.\nHealed for 20 HP.')
#                     return 1
#         else:
#             print(f'{self.name} has no potions!😭')
#             return 0
    

