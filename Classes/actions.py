import random
import json

class Action:
    def __init__(self, name, description, id, owner, target:bool, useStr: str, turns):
        
        self.name = name
        self.id = id
        self.description = description
        self.owner = owner
        self.target =  target
        #True means that it hits opponent, false means that it affects user.
        self.useStr = useStr
        self.turns = turns
        


class Items(Action):
    def __init__(self, name, description, id, owner, target, useStr, turns, stat):
        super().__init__(name, description, id, owner, target, useStr, turns) 
        self.stat = stat
        

    def __str__(self):

        return f'{self.name}: {self.description}'
    
    def __eq__(self, item2):
        return self.id == item2.id and self.owner == item2.owner
    
    def __hash__(self) -> int:
        return hash((self.id, self.owner))
        

    def itemSpawn(id, owner):
        itemFile = open('JSON/itemList.json')
        itemDict = json.load(itemFile)
        item = itemDict[id]

        return Items(item['name'], item['description'], id, owner, item['target'], item['useStr'])

    def itemUse(self, user, ftn, target):
        
        if self.target:

            if self.turns == 0:







    
        
        
class Specials(Action):
    def __init__(self, name, description, cost, type, damage, healing):
        super().__init__(self, name, description, id)
        self.cost = cost
        self.type = type
        self.damage = damage
        self.healing = healing
        