# Rock Paper Scissors Game
import sys
import random
from enum import Enum


def rps(name="PlayerOne"):
    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_rps():
        nonlocal player_wins, python_wins, name
        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        playerchoice = input(f"\n{name}, please enter ... \n1 for Rock, \n2 for Paper, \n3 for Scissors:\n\n")

        if playerchoice not in ['1', '2', '3']:
            print(f"{name}, please enter 1, 2, or 3.")
            return play_rps()


        player = int(playerchoice)

    
        # Generate computer's choice
        computerchoice = random.choice([1, 2, 3])

        computer = int(computerchoice)

        print(f"\n{name}, you chose: {RPS(player).name}.")
        print(f"Computer chose: {RPS(computer).name}.\n")

        def decide_winner(player, computer):
            nonlocal player_wins, python_wins, name
            if player == 1 and computer == 3:
                player_wins += 1
                return f"{name}, you win!💥 Rock crushes Scissors."
            elif player == 2 and computer == 1:
                player_wins += 1
                return f"{name}, you win!💥 Paper covers Rock."
            elif player == 3 and computer == 2:
                player_wins += 1
                return f"{name}, you win!💥 Scissors cut Paper."
            elif player == computer:
                return f"{name}, it's a tie!😳 Both chose the same."
            else:
                python_wins += 1
                return f"🐍💀 Python wins!💥\n Sorry {name}.."

        game_result = decide_winner(player, computer)
        print(game_result)


        nonlocal game_count
        game_count += 1

        print(f"\nGame count: {game_count}")
        print(f"\nPlayer wins: {player_wins}")
        print(f"\nPython wins: {python_wins}")

        print(f"\nPlay again?, {name}?")

        while True:
            playagain = input("Enter 'y' to continue playing or any other key to exit: ")
            if playagain.lower() == 'y':
                return play_rps()
            elif playagain.lower() == 'q' or playagain.lower() != 'y':
                break
            
        print("💥💥💥")
        print("Thanks for playing!")
        sys.exit(f"Bye! {name} 👋")

    return play_rps()


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personalized game experience."
    )
    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the person playing the game."
    )
    
    args = parser.parse_args()

    rock_paper_scissors = rps(args.name)
    rock_paper_scissors()
