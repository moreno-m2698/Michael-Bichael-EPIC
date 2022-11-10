import random
import json
import math
from Classes.actions import Items, Items2
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

