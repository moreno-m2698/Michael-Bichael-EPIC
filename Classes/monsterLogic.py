import random
import math
from Classes.unitLogic import Unit
import json

class Monster(Unit):
    def __init__(self, name: str, atk: int, defense: int, maxHp: int, magic: int, level: int, agil: int):
        super().__init__(name, atk, defense, maxHp, magic, level,agil)
        self.isEpic = False
        # self.drops = drops
        # self.baseChanceDrops = baseChanceDrops
        #come back and add these

    def __str__(self):
        
        return f'{super().__str__()} |'

    def generateMonsterJSON():
            monsterFile = open('JSON/monsterList.json')
            monsterDict = json.load(monsterFile)
    
            monsterKey = random.choice(list(monsterDict))

            monsterSubKey = random.choice(list(monsterDict[monsterKey]))
            name = f'{monsterSubKey} {monsterKey}'

            return Monster(name, monsterDict[monsterKey][monsterSubKey]['atk'], monsterDict[monsterKey][monsterSubKey]['defense'], monsterDict[monsterKey][monsterSubKey]['maxHp'],\
             monsterDict[monsterKey][monsterSubKey]['magic'], monsterDict[monsterKey][monsterSubKey]['level'], monsterDict[monsterKey][monsterSubKey]['agil'])
        
