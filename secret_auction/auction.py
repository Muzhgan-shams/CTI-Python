# Secret Auction
should_continue = True
bids_db = {}
while should_continue:
    name = input("What is your name? ")
    price = int(input("What is your bidding amount? "))
    bids_db[name] = price
    should_continue = False
