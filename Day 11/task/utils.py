import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def start_game(usr_input):
    if usr_input == "y":
        return True
    else:
        return False


def init_player_cards_and_score():
    init_player_cards = [random.choice(cards), random.choice(cards)]
    init_player_score = sum(init_player_cards)
    return [init_player_cards, init_player_score]


def display_comp_first_card():
    return random.choice(cards)

def hit_or_pass():
    inp = input("Type 'y' to get another card, type 'n' to pass: ").lower()
    if inp == "n":
        return False
    else:
        return True

def get_another_card():
    return random.choice(cards)

def display_current_cards_and_score(cards_list, score):
    print(f"Your cards: {cards_list}, current score: {score}")

def check_if_player_bust(score):
    if score > 21:
        return True
    else:
        return False

def change_11_to_1(player_cards):
    new_cards = []
    new_score = 0
    for card in player_cards:
        if card == 11:
            new_score += 1
            new_cards.append(1)
        else:
            new_cards.append(card)
            new_score += card
    return [new_cards, new_score]


def display_comp_rest_cards(comp_card):
    comp_final_cards = [comp_card]
    new_card = random.choice(cards)
    final_score = False

    while not final_score:
        if sum(comp_final_cards) < 17:
            comp_final_cards.append(new_card)
        else:
            final_score = True

    print(f"Computer final hand: {comp_final_cards}, final score: {sum(comp_final_cards)}")
    return [comp_final_cards, sum(comp_final_cards)]

def check_who_wins(comp_score, player_score):
    if not comp_score > 21 and comp_score > player_score:
        print("You Lose 😤")
    elif comp_score == player_score:
        print("It's a draw 😶")
    else:
        print("You win! 😁")

def check_if_blackjack(player_score):
    if player_score == 21:
        return False
    else:
        return True

