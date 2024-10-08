import art
import random

def play_game():
    print(art.logo)

    secret_number = random.randint(1, 100)
    print("welcome to the Guessing Game!\nI'm thinking of a number between 1 and 100")

    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    attempts = 5 if difficulty == "hard" else 10
    print(f"You have {attempts} attempts remaining to guess the number.")

    game_over = False
    while attempts > 0 and game_over == False:
        guess = int(input("Make a guess: "))
        if guess != secret_number:
            attempts -= 1
            if attempts == 0:
                print(f"You Lose. the secret number was {secret_number}\n\n")
            else:
                message = "Too High" if guess > secret_number else "Too Low"
                print(f"{message}\nYou have {attempts} attempts remaining to guess the number.")
        else:
            print(f"You got it! the answer was {secret_number}")
            game_over = True
    play_again = input("Play again? Type 'y' or 'n'").lower()
    play_game() if play_again == "y" else ""

play_game()

