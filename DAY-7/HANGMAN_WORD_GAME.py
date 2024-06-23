# HANGMAN WORD GAME

# print("welcome to Hangman word guessing game!")
# import random
# stages = ['''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  / \  |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  /    |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|   |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#   |   |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#       |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#       |
#       |
#       |
#       |
# =========
# ''']

# words=["ardvark", "baboon", "camel"]
# chosen_word=random.choice(words)


# empty_list=[]
# for _ in range(len(chosen_word)):
#     empty_list+="_"
# # print(empty_list)
# lives=6
# endofgame=False
# while not endofgame:
#     guess=input("guess a letter: ").lower()

#     for position in range(len(chosen_word)):
#         letter=chosen_word[position]
#         if letter==guess:
#             empty_list[position]=letter

#     if guess not in chosen_word:
#         lives-=1
#         if lives==0:
#             endofgame=True
#             print("You lose")

#     print(empty_list)

#     if "_" not in empty_list:
#         endofgame=True
#         print("you won")
#     print(stages[lives])