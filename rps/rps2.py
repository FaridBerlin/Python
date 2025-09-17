# Rock Paper Scissors Game
import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

playagain = True 


while playagain:

    playerchoice = input("\nEnter ... \n1 for Rock, \n2 for Paper, \n3 for Scissors:\n\n")

    player = int(playerchoice)

    if player < 1 or player > 3:
        sys.exit("Invalid choice. Please enter 1, 2, or 3.")

    # Generate computer's choice
    computerchoice = random.choice([1, 2, 3])

    computer = int(computerchoice)

    
    print("\nYou chose:" + RPS(player).name + ".")
    print("Computer chose:" + RPS(computer).name + ".\n")
    

    if player == 1 and computer == 2:
        print("You lose!😞 Paper covers Rock.")
    elif player == 1 and computer == 3:
        print("You win!💥 Rock crushes Scissors.")
    elif player == 2 and computer == 1:
        print("You win!💥 Paper covers Rock.")
    elif player == 2 and computer == 3:
        print("You lose!😞 Scissors cut Paper.")
    elif player == 3 and computer == 1:
        print("You lose!😞 Rock crushes Scissors.")
    elif player == 3 and computer == 2:
        print("You win!💥 Scissors cut Paper.")
    elif player == computer:
        print("It's a tie!😳 Both chose the same.")
    else:
        print("Invalid game state. Please try again.")

    playagain = input("\nPlay again? \nY for (yes) or \nQ for (quit): ")
   
    if playagain.lower() == 'y':
        continue
    else:
        print("💥💥💥")
        print("Thanks for playing!")
        break

print("Bye!👋")