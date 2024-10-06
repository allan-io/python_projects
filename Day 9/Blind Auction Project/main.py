from art import logo
from utils import inputs
print(logo)
# TODO-1: Ask the user for input
all_bids = {}
program_running = True

while program_running:
    bid = inputs()
    all_bids[bid[0]] = bid[1]
    program_running = bid[2]
    print("\n" * 100)

largest_bid = ["",0]
for key in all_bids:
    if all_bids[key] > largest_bid[1]:
        largest_bid[1] = all_bids[key]
        largest_bid[0] = key
print(f"the winner is {largest_bid[0]} with the bid of ${largest_bid[1]} dollars")
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary


