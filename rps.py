import random

def get_user_choice():
    """Prompt the user to enter their choice and return it."""
    choices = ["rock", "paper", "scissors"]
    while True:
        user_input = input("Make your choice (rock, paper, scissors): ").lower()
        if user_input in choices:
            return user_input
        else:
            print("Invalid choice!")

def generate_computer_choice():
    """Randomly select and return the computer's choice."""
    return random.choice(["rock", "paper", "scissors"])

def evaluate_game(user_choice, computer_choice):
    """Determine the winner based on user and computer choices."""
    outcomes = {
        ("rock", "scissors"): "Rock crushes scissors. You win!",
        ("paper", "rock"): "Paper covers rock. You win!",
        ("scissors", "paper"): "Scissors cut paper. You win!",
        ("scissors", "rock"): "Rock crushes scissors. You lose!",
        ("rock", "paper"): "Paper covers rock. You lose!",
        ("paper", "scissors"): "Scissors cut paper. You lose!",
    }

    if user_choice == computer_choice:
        return f"Both chose {user_choice}. It's a draw!"
    else:
        return outcomes.get((user_choice, computer_choice))

def play_rps():
    """Play a round of Rock Paper Scissors."""
    user_choice = get_user_choice()
    computer_choice = generate_computer_choice()
    print(f"The computer chose: {computer_choice}")
    result = evaluate_game(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    play_rps()

