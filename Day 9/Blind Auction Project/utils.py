def inputs():
    name = input("What is your name? ").capitalize()
    bid = int(input("What is your bid? "))
    another_bidder = input('Are there any other bidders? Type "yes" or "no" ').lower()
    run_program = True if another_bidder == "yes" else False
    return [name, bid, run_program]