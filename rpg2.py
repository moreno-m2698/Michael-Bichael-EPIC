import random
import json
import math
from Classes.actions import Items
from Classes.playerLogic import Hero

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

                    else:

                        print('Please give a valid input')



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

