import random
from operator import index

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices_image = [rock, paper, scissors]
choices_name = ["rock", "paper", "scissors"]

player_index = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors."))
computer_index = random.randint(0,2)

player_choice_img = choices_image[player_index]
computer_choice_img = choices_image[computer_index]

player_choice_name = choices_name[player_index]
computer_choice_name = choices_name[computer_index]

print(f"{player_choice_img}\nComputer chose: \n{computer_choice_img}")

if player_choice_name == "rock":
    if computer_choice_name == "rock":
        print("It's a Draw.")
    elif computer_choice_name == "paper":
        print("You Lose.")
    else:
        print("You Win!")

if player_choice_name == "paper":
    if computer_choice_name == "paper":
        print("It's a Draw.")
    elif computer_choice_name == "scissors":
        print("You Lose.")
    else:
        print("You Win!")

if player_choice_name == "scissors":
    if computer_choice_name == "scissors":
        print("It's a Draw.")
    elif computer_choice_name == "rock":
        print("You Lose.")
    else:
        print("You Win!")

