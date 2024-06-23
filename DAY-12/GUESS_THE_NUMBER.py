# PROJECT: GUESS THE NUMBER

# print("Welcome to the number guessing game!")
# import random
# number_to_be_guessed= random.randint(1,100)
# print("I'm thinking of a number between 1 and 100")
# end_of_gam= False
# counter=10
# counter_hard=5


# level= input("Choose difficulty: Type 'easy' or 'hard' \n")
# guess= int(input("Make a guess: \n"))
# if level=="easy":
#     if number_to_be_guessed>guess:
#         print("Too low.")
#     elif number_to_be_guessed<guess:
#         print("Too high.")
#     if guess==number_to_be_guessed:
#             end_of_gam=True
#             print(f"You have won, and the number is {number_to_be_guessed} ")
#     else:
#         while not end_of_gam:
#             for i in range(10):
#                 counter-=1
#                 print(f"You have {counter} attempts left,")
#                 guess_again= int(input("Guess again: \n"))
#                 if guess_again>number_to_be_guessed:
#                     print("Too high.")
#                 elif guess_again<number_to_be_guessed:
#                     print("Too low.")
#                 if guess_again== number_to_be_guessed:
#                     end_of_gam=True
#                     print(f"You have won, and the number is {number_to_be_guessed}")
#                     break
                    
#                 if counter==1:
#                     end_of_gam= True
#                     print("You have run out of attempts")
#                     break
# elif level=="hard":
#     if number_to_be_guessed>guess:
#         print("Too low.")
#     elif number_to_be_guessed<guess:
#         print("Too high.")
#     if guess==number_to_be_guessed:
#             end_of_gam=True
#             print(f"You have won, and the number is {number_to_be_guessed} ")
#     else:
#         while not end_of_gam:
#             for i in range(5):
#                 counter_hard-=1
#                 print(f"You have {counter_hard} attempts left,")
#                 guess_again= int(input("Guess again: \n"))
#                 if guess_again>number_to_be_guessed:
#                     print("Too high.")
#                 elif guess_again<number_to_be_guessed:
#                     print("Too low.")
#                 if guess_again== number_to_be_guessed:
#                     end_of_gam=True
#                     print(f"You have won, and the number is {number_to_be_guessed}")
#                     break
                    
#                 if counter_hard==1:
#                     end_of_gam= True
#                     print("You have run out of attempts")
#                     break
# Better Solution
# import random

# # guess= int(input("Make a guess: "))
# answer= random.randint(1,100)
# EASY_LEVEL_TERMS= 10
# HARD_LEVEL_TERMS= 5

# def check_answer(guess, answer, turns):
#     if guess>answer:
#         print("Too High.")
#         return turns-1
#     elif guess<answer:
#         print("Too low.")
#         return turns-1
#     else:
#         print(f"You got it!, the answer was {answer}")

# def set_difficulty():
#     level=input("Choose a difficulty: type 'easy' or 'hard': ")
#     if level=="easy":
#         return EASY_LEVEL_TERMS
#     elif level=="hard":
#         return HARD_LEVEL_TERMS
# def game():
#     print("Welcome to Number Guessing Game!")
#     print("I'm thinking of a number between 1 and 100")
#     turns= set_difficulty()
    
#     guess=0
#     while guess!=answer:
#         print(f"You have {turns} attempts left to guess the number.")
#         guess= int(input("Make a guess: "))
#         turns= check_answer(guess, answer, turns)
#         if turns==0:
#             print("You've run out of guesses, you loose")
#             return
#         elif guess!=answer:
#             print("Guess again.")
            
# game()  