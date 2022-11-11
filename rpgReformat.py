import random
import json
import math
from Classes.actions import Items
from Classes.playerLogic import Hero
from Classes.monsterLogic import Monster
import gameLogic




def main():            

    turn = 0


    print("Welcome to Michael and Bichael's slime massacre RPG.\nDo you want to play as Michael or Bichael?")
    heroName = input()
        

    if heroName == 'Michael' or heroName == 'Bichael':

        hero = Hero.heroSelection(heroName)
        print(hero)

        print('Your epic begins now!')

        gameLogic.encounter()

            
if __name__ == '__main__':
    main()       