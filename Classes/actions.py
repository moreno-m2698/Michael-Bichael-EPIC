import random
import json
from dataclasses import dataclass
from Classes.unitLogic import Unit


        
# An item is defined from a JSON and the main thing it has is its function/what it does 

# lambdas only give back expressions, they dont mutate any state



class ItemFuncs:
    def healthPot(user, target):
        user.currentHp += 20
        print(f"{user.name} has healed for 20 HP!")

    def throwRock(user, target):
        damage = random.randint(0,19) + user.atk - target.defense/2
        target.currentHp -= damage
        print(f"{user.name} threw the rock for {damage}! {target.name} is veggie :(")

    def manaPot(user, target):
        user.manaCurrent += 10
        print(f"{user.name} has restored 10 MP!")
         

    def getFuncDictionary():

        fDict = {"20heal": ItemFuncs.healthPot, "throwrock": ItemFuncs.throwRock, "10mana": ItemFuncs.manaPot}

        return fDict

def critChance(user):
    chanceCap = 50 - (2 * user.luck) - user.agil
    if chancealter <= 1:
        chancealter = 1
    critChance = 1 == random.randint(1, chanceCap)
    if critChance:
        print('It was a critical hit!')
    return critChance


class MoveFuncs:


    def slash(user, target):
        user.manaCurrent -= 5
        damage = int(user.atk * 1.5)
        print(f'{user.name} slashed at {target.name}!')
        if not(Unit.dodge(target)):
            if critChance(user):
                damage = damage * 2
            target.currentHp -= damage
            print(f'{target.name} took {damage} damage.')
    
    def smallheal(user, target):
        heal = int(user.maxHp / 6)
        user.currentHp += heal
        user.manaCurrent += 4
        print(f'{user.name} healed for {heal} health.')
    
    def icicle(user, target):
        damage = int(user.magic * 3 / 4)
        user.manaCurrent -= 5
        print(f'{user.name} launched an icicle at {target.name}')
        if not(Unit.dodge(target)):
            if critChance(user):
                damage * 2
            target.currentHp -= damage
            target.agil -=1
            print(f"{target.name} took {damage} damage.")
    
    def fireball(user, target):
        mpCost = int(user.manaCurrent / 5)
        damage = int(user.magic * 1.2 + mpCost)
        user.manaCurrent -= mpCost
        print(f'{user.name} launched a fireball at {target.name}')
        if not(Unit.dodge(target)):
            if critChance(user):
                damage * 2
            target.currentHp -= damage
            print(f"{target.name} took {damage} damage.")

    def ram(user,target):
        damage = int(user.defense + (user.atk * 1.2))
        user.manaCurrent -= 5
        print(f'{user.name} charged {target.name}')
        if critChance(user):
             damage * 2
        target.currentHp -= damage
        print(f"{target.name} took {damage} damage.")
    
    def getMoveDict():

        fDict = {
           a : MoveFuncs.slash,
           b : MoveFuncs.smallheal,
           c : MoveFuncs.icicle,
           d : MoveFuncs.fireball,
           e : MoveFuncs.ram
        }
        return fDict


    


@dataclass
class Item:
    name: str
    description: str
    useId: str
    
    def __str__(self):

        return f'{self.name}: {self.description}'
    
    #give back a list from every single item in the json
    def itemSpawn(functionDict):
        itemFile = open('JSON/itemList.json')
        itemDict = json.load(itemFile)
        itemReturnList = {}

        for itemKey in itemDict.keys():
            loadedJson = itemDict[itemKey]

            newItem = Item(loadedJson["name"], loadedJson["description"], loadedJson["useId"])

            itemReturnList[itemKey] = newItem

        return itemReturnList

    def use(self, user, target):
        ItemFuncs.getFuncDictionary()[self.useId](user, target)

@dataclass
class Specials:
    name: str
    description: str
    useId: str
