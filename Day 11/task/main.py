import art, utils

start_game_input = input("Do you want to play a game of blackjack? type 'y' or 'no': ").lower()
# start_game variable is a boolean that indicates if player wants to start a game
# while start game is True player should play until win/lose/draw
# after round is complete program should check with user again
start_game = utils.start_game(start_game_input)

def play_again():
    inp = input("Would you like to play another game of blackjack? Type 'y' for yes, or 'n' for no.")
    if inp:
        run_blackjack()

#check if comp has blackjack after player enters 'n' and wa

    # if the start_game var is True, all game logic should happen until conclusion

def run_blackjack():

    # while game is not over, player should be able to choose another card
    # game is over when player busts or does not want another card
    game_over = False
    print(art.logo)

    player_init_cards_and_score = utils.init_player_cards_and_score()
    player_init_cards = player_init_cards_and_score[0]
    player_init_score = player_init_cards_and_score[1]
    comp_init_score = utils.display_comp_first_card()

    print(f"Your cards: {player_init_cards}, current score: {player_init_score}")
    print(f"Computer's first card: {comp_init_score}")

    player_current_cards = player_init_cards
    player_current_score = player_init_score
    comp_current_score = comp_init_score
    comp_current_cards = [comp_init_score]
    start_game = utils.check_if_blackjack(player_init_score)

    if not start_game:
        print("You have blackjack")
        restart_input = input("Do you want to play a game of blackjack? type 'y' or 'no': ").lower()
        restart_game = utils.start_game(restart_input)
        if restart_game:
            run_blackjack()



    while not game_over and start_game:

        bust = False

        another_card_prompt = utils.hit_or_pass()
        if not another_card_prompt:
            comp_final_cards_and_score = utils.display_comp_rest_cards(comp_init_score)
            comp_current_cards = comp_final_cards_and_score[0]
            comp_current_score = comp_final_cards_and_score[1]
            comp_has_11 = 11 in comp_current_cards
            if comp_has_11:
                if comp_current_score == 21:
                    game_over = True
                    print("Computer has blackjack 💩")
                result = utils.change_11_to_1(comp_current_cards)
                comp_current_cards = result[0]
                comp_current_score = result[1]
            print(comp_current_score)
            utils.check_who_wins(comp_current_score, player_current_score)
            game_over = True
        if not game_over:
            new_card = utils.get_another_card()
            player_current_cards.append(new_card)
            player_current_score += new_card
            bust = utils.check_if_player_bust(player_current_score)
        if bust:
            player_has_11 = 11 in player_current_cards
            if player_has_11:
                result = utils.change_11_to_1(player_current_cards)
                player_current_cards = result[0]
                player_current_score = result[1]
            else:
                # run_blackjack()
                game_over = True
                print("You Lose")
                print(f"Computer's final hand: {comp_current_cards}, final score: {comp_current_score}")
                play_again()
        # change this around so you lose is the last thing you see
        utils.display_current_cards_and_score(player_current_cards, player_current_score)

    # after we should run check_who_wins
    #display who wins and why "opponent went over", "you went over", and always
    # your final hand and your final score, computers final hand, computer final score
if start_game:
    run_blackjack()