# PROJECT: BLACKJACK CARD GAME

# import random
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# def dealer_card():
#     card= random.choice(cards)
#     return card

# def calculate_score(cards):
#     if len(cards)==2 and sum(cards)==21:
#         return 0
#     if 11 in cards and sum(cards)>21:
#         cards.remove(11)
#         cards.append(1)
#     return sum(cards)

# def compare(user_score, computer_score):
#     if user_score>21 and computer_score>21:
#         return "you went over , you lose"
#     elif computer_score==user_score:
#         return "Draw"
#     elif user_score==0:
#         return "win, its a blackjack!"
#     elif computer_score==0:
#         return "computer wins with blackjack"
#     elif user_score>21:
#         return "you went over, You lose!"
#     elif computer_score>21:
#         return "opponent went over, You win!"
#     elif user_score>computer_score:
#         return "you win!"
#     else:
#         return "You lose"

# user_cards=[]
# dealer_cards=[]
# end_of_game= False

# for i in range(2):
#     user_cards.append(dealer_card())
#     dealer_cards.append(dealer_card())

# while not end_of_game:
#     user_score=calculate_score(user_cards)
#     computer_score=calculate_score(dealer_cards)
#     print(f"your cards: {user_cards} and current score {user_score}")
#     print(f"computers first card: {dealer_cards[0]} ")
    
#     if user_score==0 or computer_score==0 or user_score>21:
#         end_of_game= True
#     else:
#         user_should_deal=input("type 'y' to deal or type 'n' to pass \n")
#         if user_should_deal=="y":
#             user_cards.append(dealer_card())
#         else:
#             end_of_game= True
# while computer_score!=0 and computer_score<17:
#         dealer_cards.append(dealer_card())
#         computer_score= calculate_score(dealer_cards)

# print(f"your final hand: {user_cards} and your final score: {user_score}")
# print(f"computer's final hand: {dealer_cards} and computer's final score {computer_score}")

# print(compare(user_score, computer_score))