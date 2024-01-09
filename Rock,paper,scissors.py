import random

# This function prompts the user for a pick
def get_player_choice():
    player_choice = input("Rock, paper, scissors, shoot (rock, paper, or scissors): ")
    while player_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice.")
        player_choice = input("Rock, paper, scissors, shoot (rock, paper, or scissors): ")
    return player_choice

# This function prompts the computer for a pick
def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

# This function gets to determine the winner by comparing responses from both players
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "A tie"
    elif (
            (player_choice == "rock" and computer_choice == "scissors") or
            (player_choice == "paper" and computer_choice == "rock") or
            (player_choice == "scissors" and computer_choice == "paper")
    ):
        return "Player wins!"
    else:
        return "Computer wins!"

# This function welcomes the user and afterwards prints out answers from both players and declares the winner.
def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    player_choice =get_player_choice()
    computer_choice = get_computer_choice()
    print(f"You chose {player_choice}.")
    print(f"I chose {computer_choice}.")
    result = determine_winner(player_choice, computer_choice)
    print(result)

# Call the play_game function to start the game
play_game()
