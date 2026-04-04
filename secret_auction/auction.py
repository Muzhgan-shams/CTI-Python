# Secret Auction Game

print(r"""
   ==========================================
        ____   _     _     _       
       | __ ) (_) __| | __| | ___  
       |  _ \ | |/ _` |/ _` |/ _ \ 
       | |_) || | (_| | (_| |  __/ 
       |____/ |_|__,_|\__,_|\___|  
                                   
        $$$   SECRET BIDS   $$$
        Place your hidden offers...
        Who will win the prize?
   ==========================================
""")


continue_bidding = True
bids_db = {}


def get_highest_bid(bids):
    winner = ""
    highest_bid = 0
    for bidder in bids:
        bid_amount = bids[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with the bid of ${highest_bid}")


while continue_bidding:
    name = input("What is your name? ")
    price = int(input("What is your bidding amount? "))
    bids_db[name] = price
    should_continue = input(
        "Are there any bidders? Type 'Yes' or 'No'\n").lower().strip()
    if should_continue == "no":
        print()
        continue_bidding = False
        get_highest_bid(bids_db)
    elif should_continue == "yes":
        print("\n" * 30)
