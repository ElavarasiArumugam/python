def highest_bidding(bids):
    max_bid = 0
    winner = ""
    for bidder_name, bidder_amount in bids.items():
        if bidder_amount > max_bid:
            max_bid = bidder_amount
            winner = bidder_name
    return max_bid, winner

print("Welcome to the auction!")
bidding = True
auction = {}

while bidding:
    bidder_name = input("What is your name? ")
    bidder_amount = int(input("What amount do you want to bid? "))
    auction[bidder_name] = bidder_amount

    next_bidder = input("Is there any other bidder? Type Yes or No: ").lower()
    if next_bidder == "yes":
        bidding = True
    elif next_bidder == "no":
        bidding = False
    else:
        print("Invalid input. Assuming no more bidders.")
        bidding = False

max_amount, winner = highest_bidding(auction)
print(f"The highest bidding amount is ₹{max_amount}, by {winner}.")
