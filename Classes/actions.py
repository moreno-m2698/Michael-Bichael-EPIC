import random
import json
from dataclasses import dataclass


        
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

        fDict = {"20heal": ItemFuncs.healthPot, "throwrock": ItemFuncs.throwRock}

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









    
        
        
class Specials:
    def __init__(self, name, description, cost, type, damage, healing):
        super().__init__(self, name, description, id)
        self.cost = cost
        self.type = type
        self.damage = damage
        self.healing = healing
        
    def useSpecial():
        pass