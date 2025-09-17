# Rock Paper Scissors Game
import sys
import random
from enum import Enum

game_count = 0

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
    
    def decide_winner(player, computer):
        if player == 1 and computer == 3:
            return "You win!💥 Rock crushes Scissors."
        elif player == 2 and computer == 1:
            return "You win!💥 Paper covers Rock."
        elif player == 3 and computer == 2:
            return "You win!💥 Scissors cut Paper."
        elif player == computer:
            return "It's a tie!😳 Both chose the same."
        else:
            return "🐍💀 Python wins!💥"

    game_result = decide_winner(player, computer)
    print(game_result)


    global game_count
    game_count += 1

    print("\nGame count:" + str(game_count))

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
