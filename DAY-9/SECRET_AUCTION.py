#SECRET AUCTION PROGRAM

# bid={}
# bidding_finished= False

# def highest_bidder(bid_recorder):
#     highest_bid=0
#     winner=""

#     for bidder in bid_recorder:
#         bid_amount= bid_recorder[bidder]
#         if bid_amount>highest_bid:
#             highest_bid= bid_amount
#             winner= bidder

#     print(f"The winner is {winner} with a bid of {bid_amount}")

# while not bidding_finished:
#     name= input("What is your name? \n")
#     price= int(input("What is your price? \n"))
#     bid[name]= price

#     should_conitinue= input("Is there another bidder? 'yes' or 'no' .\n")
#     if should_conitinue=="no":
#         bidding_finished= True
#         highest_bidder(bid)