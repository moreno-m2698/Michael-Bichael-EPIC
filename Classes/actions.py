import random
import json

class Action:
    def __init__(self, name, description, id, owner, useStr):
        
        self.name = name
        self.id = id
        self.description = description
        self.owner = owner
        self.useStr = useStr
        
        
actionFtns = {
    
    "2000": lambda user, target: [user.currentHp + 20, target.currentHp],
    "2001": lambda user, target: [user.manaCurrent + 10, target.currentHp],
    "2002": lambda user, target: [user.currentHp, target.currentHp - random.randint(1,9)]



}



class Items(Action):
    def __init__(self, name, description, id, owner, useStr, useId, stat):
        super().__init__(name, description, id, owner, useStr)
        self.useId = useId
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

        return Items(item['name'], item['description'], id, owner, item['useStr'], item['useId'], item['stat'])

    def use(self, user, target):
        print(f"{user.name} {self.useStr}")
        resultList = actionFtns[self.useId](user, target)
        return resultList








    
        
        
class Specials(Action):
    def __init__(self, name, description, cost, type, damage, healing):
        super().__init__(self, name, description, id)
        self.cost = cost
        self.type = type
        self.damage = damage
        self.healing = healing
        
    def use():
        pass