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

