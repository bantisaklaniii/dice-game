import random

def roll_dice():
    """Simulate rolling a dice."""
    return random.randint(1, 6)

def play_game():
    print("Welcome to the Dice Rolling Game!")
    player_score = 0
    computer_score = 0

    while True:
        input("Press Enter to roll the dice.")
        player_dice1 = roll_dice()
        player_dice2 = roll_dice()
        player_total = player_dice1 + player_dice2
        computer_dice1 = roll_dice()
        computer_dice2 = roll_dice()
        computer_total = computer_dice1 + computer_dice2

        print(f"\nYou rolled: {player_dice1}, {player_dice2} (Total: {player_total})")
        print(f"Computer rolled: {computer_dice1}, {computer_dice2} (Total: {computer_total})")

        if player_total > computer_total:
            print("Congratulations! You win this round!")
            player_score += 1
        elif player_total < computer_total:
            print("Sorry, the computer wins this round.")
            computer_score += 1
        else:
            print("It's a tie!")

        print(f"Your score: {player_score} | Computer score: {computer_score}\n")

        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    play_game()
