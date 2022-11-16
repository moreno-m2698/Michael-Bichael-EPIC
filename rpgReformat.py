import random
import json
import math
from Classes.actions import Items
from Classes.playerLogic import Hero
from Classes.monsterLogic import Monster
import gameLogic
import time



def main():            

    turn = 0


    print("Welcome to Michael and Bichael's slime massacre RPG.\nDo you want to play as Michael or Bichael?")
    heroName = input()
        

    if heroName == 'Michael' or heroName == 'Bichael':

        hero = Hero.heroSelection(heroName)
        print(hero)

        print('Your epic begins now!')

        while True:
            # This loop makes the game infinite

            enemy = gameLogic.encounter()

            while not(hero.currentHp <= 0 or enemy.currentHp <= 0):

                if turn == 0:

                    # Player turn
                    print(hero)
                    print(enemy)

                    
                    action = int(input(f'What will {heroName} do?\n1. Attack\n2. Pass\n3. Look at Inventory \n4. End Game \n'))

                    if action == 1:
                        time.sleep(1)
                        Hero.attack(hero,enemy)

                        turn = 1

                        if enemy.currentHp <= 0:

                            print(f'You defeated the {enemy.name}!')
                            gameLogic.rewards(hero,enemy)
                            
                            break

                    elif action == 2:

                        Hero.passTurn(hero)
                        turn = 1

                    elif action == 3:
                        if hero.inventory == {}:
                            print(f"{heroName}'s inventory is empty.")
                        else:
                            index = Hero.inventoryAccess(hero)
                            inventoryls = list(hero.inventory)
                            
                            while True:
                                choice = input(f'Type the name of the item that you want to use or type "close" to close the inventory\n')
                                if choice.isdigit() and not(int(choice) <= 0) and not(int(choice) >= index):
                                    choice = int(choice)
                                    #Write code for item use
                                    action = inventoryls[choice - 1]
                                    # Now we get into the item use code

                                    

                                    print(f'{heroName} used a {action.name}.')
                                    break
                                
                                elif choice == 'close':
                                    break
                                else:
                                    print('Please give a valid input.')

                        
                        



                    elif action == 4:
                        break

                    else:

                        print('Please give a valid input')



                elif turn == 1:
                        
                    Monster.attack(enemy,hero)

                    turn = 0

                if hero.currentHp <= 0:
                    print(f'{heroName} blacks out....\n Game Over')
                    break

            
if __name__ == '__main__':
    main()       