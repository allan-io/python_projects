import random
from art import logo
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "It's a draw 😶"
    elif c_score == 0:
        return "You lose. Computer has blackjack 🤯"
    elif u_score == 0:
        return "You have blackjack, you win 😎"
    elif u_score > 21:
        return "You went over 21, you lose 😭"
    elif c_score > 21:
        return "Computer went over 21, you win 😁"
    elif u_score > c_score:
        return "You Win! 🎉"
    else:
        return "You Lose 😭"


def play_blackjack():
    print(logo)
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}\nComputer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            deal_new_card = input("Do you want to draw another card? Type 'y' for yes, 'n' for no: \n").lower()
            if deal_new_card == "y":
                user_cards.append(deal_card())
            else:
                game_over = True

    while computer_score < 17 and computer_score != 0:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final cards: {user_cards}, final score: {user_score}")
    over_21_card = []
    if user_score > 21:
        over_21_card.append(computer_cards[0])
    print(f"Computer final cards: {computer_cards if user_score <= 21 else over_21_card}, final score: {computer_score if user_score <= 21 else computer_cards[0]}")
    print(f"{compare(user_score, computer_score)}\n")

while input("Do you want to play a game of Blackjack? type 'y' or 'n': ").lower() == 'y':
    print("\n" * 20)
    play_blackjack()
