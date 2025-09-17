# Rock Paper Scissors Game
import sys
import random
from enum import Enum

def play_rps():
    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    

    playerchoice = input("\nEnter ... \n1 for Rock, \n2 for Paper, \n3 for Scissors:\n\n")

    if playerchoice not in ['1', '2', '3']:
        print("Invalid input. Please enter 1, 2, or 3.")
        return play_rps()


    player = int(playerchoice)

   
    # Generate computer's choice
    computerchoice = random.choice([1, 2, 3])

    computer = int(computerchoice)

    print("\nYou chose:" + RPS(player).name + ".")
    print("Computer chose:" + RPS(computer).name + ".\n")
    
    if player == 1 and computer == 3:
        print("You win!💥 Rock crushes Scissors.")
    elif player == 2 and computer == 1:
        print("You win!💥 Paper covers Rock.")
    elif player == 3 and computer == 2:
        print("You win!💥 Scissors cut Paper.")
    elif player == computer:
        print("It's a tie!😳 Both chose the same.")
    else:
        print(" Python wins!💥")

    print("\nPlay again?")     
    
    while True:
        playagain = input("Enter 'y' to continue playing or any other key to exit: ")
        if playagain.lower() == 'y':
            return play_rps()
        elif playagain.lower() == 'q' or playagain.lower() != 'y':
            break
        
    print("💥💥💥")
    print("Thanks for playing!")
    sys.exit("Bye!👋")


play_rps()
