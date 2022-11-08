import random
import json

#Michael and Bichael the EPIC MINI Saga RPG

#Hero class, hero is going to have hp, attk, defense, name

#Make a slime class

#Ask user whether they want to play as Bichael or Michael

#Enter a gameloop where you fight vs a slime, if you reduce the slime's hp to 0 you win and the game stops, if it reduces your hp you lose and u suck

# Every loop, you get to either attack (hit the slime), or do nothing

#You and the slime take turns, the slime can only attack you, you always attack before the slime (You go first)

#Attacks from either you or the slime can be critical hits and deal double damage

#User is asked for input every turn on whether they want to attack or pass, every attack and dmg calculation is printed to the screen

#dmg calculation method


#Unit is the super class / parent class of slime and hero
class Unit:
    def __init__(self, name: str, atk: int, defense: int, maxHp: int):
        self.name = name
        self.atk = atk
        self.defense = defense
        self.maxHp = maxHp
        self.currentHp = self.maxHp

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
    def __init__(self, name: str, atk: int, defense: int, maxHp: int):
        super().__init__(name, atk, defense, maxHp)
        self.healthpots = 5
        self.slimesKilled = 0
        

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
        heroFile = open('hero.json')
        heroDict = json.load(heroFile)

        hero = heroDict[name]

        return Hero(name, hero['atk'], hero['defense'], hero['maxHp'])


    
    def findPotion(self, amount):

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
                hero.findPotion(1)


        else:
            hero.findPotion(2)

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
            



def main():            

    turn = 0


    print("Welcome to Michael and Bichael's slime massacre RPG.\nDo you want to play as Michael or Bichael?")
    heroName = input()
        

    if heroName == 'Michael' or heroName == 'Bichael':

        hero = Hero.heroSelection(heroName)


        print('Your epic begins now!')

            
        while True:

            # enemy = Slime.generateSlimeJSON()
            enemy = Slime.generateSlime()

            turn = 0

            print(f'A {enemy.name} slime appeared!')


                
                
            # Create battle system

            # Put some flavor text to show that you've encountered a wild slime.
            while not(hero.currentHp <= 0 or enemy.currentHp <= 0):



                if turn == 0:

                    # Player turn 
                    print(hero)
                    print(enemy)

                    action = int(input(f'What will {heroName} do?\n1. Attack\n2. Pass\n3. Use Potion \n4. End Game \n'))

                    if action == 1:

                        Hero.attack(hero,enemy)

                        turn = 1

                        if enemy.currentHp <= 0:

                            print(f'{enemy.name} slime died.')

                            Slime.potionDrop(enemy,hero)
                            break

                    elif action == 2:

                        Hero.passTurn(hero)
                        turn = 1

                    elif action == 3:
                        
                        turn = hero.potionUse()

                    elif action == 4:
                        break



                elif turn == 1:
                        
                    Slime.attack(enemy,hero)

                    turn = 0

                if hero.currentHp <= 0:
                    print(f'{heroName} blacks out....\n Game Over')
                    break
                

                
            
            if hero.currentHp <= 0:
                break

            if action == 4:
                print('Thank you for playing!')
                break
    else:
        print('booo')


if __name__ == '__main__':
    main()       

