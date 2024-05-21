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
        return "draw"
    else:
        return "win" if outcomes.get((user_choice, computer_choice)) else "lose"

def play_rps():
    """Best of three."""
    print("Welcome to Rock Paper Scissors! The game is best of three rounds.")
    user_wins = 0
    computer_wins = 0
    
    # Loop for playing until one player wins two rounds
    while user_wins < 2 and computer_wins < 2:
        user_choice = get_user_choice()
        computer_choice = generate_computer_choice()
        print(f"The computer chose: {computer_choice}")
        result = evaluate_game(user_choice, computer_choice)

        # Update score based on the result of the round
        if result == "win":
            user_wins += 1
            print("You win!")
        elif result == "lose":
            computer_wins += 1
            print("Computer wins!")
        else:
            print("Draw!")

        # Display the score after each round
        print(f"Score: You -{user_wins}, Computer -{computer_wins}")
    
    # Determine the winner of the game
    print("\nGame over!")
    if user_wins > computer_wins:
        print("You win the game!")
    else:
        print("Computer wins the game!")

if __name__ == "__main__":
    play_rps()

