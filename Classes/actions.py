import random

class Action:
    def __init__(self, name, description, id):
        
        self.name = name
        self.id = id
        self.description = description
        


class Items(Action):
    def __init__(self, name, description, id, baseChance):
        super().__init__(self, name, description, id)
        self.baseChance = baseChance
        self.amount = 3
        
    def itemDrop(self, hero, monster):
        if monster.epic:
            if random.randint(1,self.baseChance) == 1:
                hero.findItem(1)


        else:
            hero.findItem(3)    
        
        
class Specials(Action):
    def __init__(self, name, description, cost, type, damage, healing):
        super().__init__(self, name, description, id)
        self.cost = cost
        self.type = type
        self.damage = damage
        self.healing = healing
        