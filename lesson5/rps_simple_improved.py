#!/usr/bin/env python3
"""
Improved Rock Paper Scissors Game - Simple Version
Better than original with input validation, emojis, and cleaner code
"""

import sys
import random
from enum import Enum

class RPS(Enum):
    """Rock Paper Scissors choices with emojis"""
    ROCK = (1, "🪨")
    PAPER = (2, "📄") 
    SCISSORS = (3, "✂️")
    
    def __init__(self, num, emoji):
        self.num = num
        self.emoji = emoji

def get_choice_display(choice_num):
    """Get emoji and name for a choice number"""
    choices = {
        1: ("🪨", "Rock"),
        2: ("📄", "Paper"),
        3: ("✂️", "Scissors")
    }
    return choices.get(choice_num, ("❓", "Unknown"))

def get_player_input():
    """Get and validate player input"""
    while True:
        try:
            print("\nChoose your weapon:")
            print("1 🪨 Rock")
            print("2 📄 Paper") 
            print("3 ✂️ Scissors")
            
            choice = input("\nEnter your choice (1-3): ").strip()
            player = int(choice)
            
            if 1 <= player <= 3:
                return player
            else:
                print("❌ Invalid choice! Please enter 1, 2, or 3.")
        except ValueError:
            print("❌ Invalid input! Please enter a number.")

def determine_winner(player, computer):
    """Determine the winner and return appropriate message"""
    player_emoji, player_name = get_choice_display(player)
    computer_emoji, computer_name = get_choice_display(computer)
    
    print(f"\n🎯 You chose: {player_emoji} {player_name}")
    print(f"🤖 Computer chose: {computer_emoji} {computer_name}")
    
    if player == computer:
        return "🤝 It's a tie! Both chose the same."
    
    # Define winning combinations
    wins = {
        (1, 3): "💥 Rock crushes Scissors!",
        (2, 1): "📦 Paper covers Rock!",
        (3, 2): "✂️ Scissors cut Paper!"
    }
    
    if (player, computer) in wins:
        return f"🎉 You win! {wins[(player, computer)]}"
    else:
        # Computer wins - find the winning message
        for (winner, loser), message in wins.items():
            if winner == computer and loser == player:
                return f"😞 You lose! {message}"
    
    return "❓ Something went wrong!"

def play_game():
    """Main game function"""
    print("🎮 Welcome to Rock Paper Scissors! 🎮")
    print("=" * 40)
    
    # Get player choice
    player = get_player_input()
    
    # Generate computer choice
    computer = random.choice([1, 2, 3])
    
    # Show result
    result = determine_winner(player, computer)
    print(f"\n{result}")

def main():
    """Entry point with error handling"""
    try:
        play_game()
    except KeyboardInterrupt:
        print("\n\n👋 Game interrupted. Goodbye!")
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")

if __name__ == "__main__":
    main()
