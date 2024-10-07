import art, utils

start_game_input = input("Do you want to play a game of blackjack? type 'y' or 'no': ").lower()
# start_game variable is a boolean that indicates if player wants to start a game
# while start game is True player should play until win/lose/draw
# after round is complete program should check with user again
start_game = utils.start_game(start_game_input)

def display_current_score():
    print("Current Score")

def display_comp_first_card():
    print("Computer First Card")

def display_comp_rest_cards():
    print("Rest of computers cards")

def check_if_player_bust():
    print("player bust")
#
def check_who_wins():
    print("Who wins")

def hit_or_pass():
    inp = input("Type 'y' to get another card, type 'n' to pass: ")
    return inp

# if the start_game var is True, all game logic should happen until conclusion
if start_game:
    # while game is not over, player should be able to choose another card
    # game is over when player busts or does not want another card
    game_over = False
    print(art.logo)
    while not game_over:
        player_init_cards_and_score = utils.init_player_cards_and_score()
        player_init_cards = player_init_cards_and_score[0]
        player_init_score = player_init_cards_and_score[1]
        print(f"Your cards: {player_init_cards}, current score: {player_init_score}")
        # display the computers first card
        # keep track of player cards and scores and computer cards and scores
        another_card_prompt = hit_or_pass()
        #if "y", get another card from the cards list check if score is <= 21
        # if <= 21 add another card to card display and add score
        # else if score is over 21 check if any 11s to use as 1 instead A = 11 or 1
        # if no 11 to change to 1 game_over = True, you lose
        # else if "n" run function display_comp_rest_cards this also calcs comp score
        # after we should run check_who_wins
        #display who wins and why "opponent went over", "you went over", and always
        # your final hand and your final score, computers final hand, computer final score