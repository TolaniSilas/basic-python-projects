# Dice Rolling Simulator

import random

print("Welcome to Dice Rolling Game!")
roll_result1 = random.randrange(1,7)
roll_result2 = random.randrange(1,7)

def DiceRollingSimulator():
    help = input("Do you need help? Yes/No : ").title()

    if "Yes" == help:
        print("""
    To roll a dice - Enter "True"
    To Quit - Enter "False"
      """)
        
        roll_dice = input("Roll a dice: ").title()
        
        if roll_dice == "True":
            roll = 2
            while roll > 0:
                if roll == 2:
                    print("The first dice roll result is:",roll_result1)
                elif roll == 1:
                    print("The second dice roll result is:",roll_result2)
                roll -= 1
            print("The outcome of the dice is: ",roll_result1 + roll_result2)
        
        elif roll_dice == "False":
            print("You are out of the game!")
        
        else:
            print("You are out of the game!",end=" ")
            print(""""Enter "True" or "False".""")
            
    else: 
        print("Please Enter 'Yes' for help! ")


DiceRollingSimulator()









 

