import random
import math
from unitLogic import Unit

class Monster(Unit):
    def __init__(self, atk: int, defense: int, maxHp: int, name: str, drops: str, self.baseChanceDrops):
        super().__init__(name, atk, defense, maxHp)
        self.isEpic = False
        self.drops = drops
        self.baseChanceDrops

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

