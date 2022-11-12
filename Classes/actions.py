import random
import json

class Action:
    def __init__(self, name, description, id):
        
        self.name = name
        self.id = id
        self.description = description
        


class Items(Action):
    def __init__(self, name, description, id):
        super().__init__(name, description, id) 

    def __str__(self):

        print(f'{self.name}: {self.description}')
        

    def itemSpawn(id):
        itemFile = open('JSON/itemList.json')
        itemDict = json.load(itemFile)
        item = itemDict[id]

        return Items(item['name'], item['description'], id)
    


    
        
        
class Specials(Action):
    def __init__(self, name, description, cost, type, damage, healing):
        super().__init__(self, name, description, id)
        self.cost = cost
        self.type = type
        self.damage = damage
        self.healing = healing
        