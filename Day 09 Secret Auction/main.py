def find_highest_bidder(bidding_record):
    max_bid = 0
    max_bider = ''
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > max_bid:
            max_bid = bid_amount
            max_bider = bidder
    print(f"The winner is {max_bider} with a bid of ${max_bid}")


continue_bidding = True
bids = {}

while continue_bidding:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print("\n" * 20)



