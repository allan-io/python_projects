from random import randint

from game_data import data
import art
import random

def check_correct_answer(a_count, b_count, player_answer):
    most_followers = "a" if a_count > b_count else "b"
    return True if player_answer == most_followers else False

def choose_new_profile():
    print("new profile")

def play_game():
    print(art.logo)
    a = random.choice(data)
    b = random.choice(data)
    game_over = False
    score = 0


    while not game_over:
        print(f"Compare A: {a["name"]}, a {a["description"]}, from {a["country"]}")
        print(art.vs)
        print(f"Against B: {b["name"]}, a {b["description"]}, from {b["country"]}")
        player_answer = input("Who has more followers? Type 'B' or 'A'")
        result = check_correct_answer(a["follower_count"], b["follower_count"], player_answer)
        if result:
            score += 1
            print("\n" * 20)
            print(f"You're right! Current score: {score}")
            a = b
            b = random.choice(data)
        else:
            print("\n" * 20)
            game_over = True
            print(f"Sorry, that's wrong. Final score {score}")

play_game()



