# PYTHON PASSWORD GENERATOR

# print("welcome to pypassword generator!")
# import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
#            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
#            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
#            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# symbols = ['!', '@', '#', '$', '%', '+', '&', '*', '(', ')']

# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# nr_letters=int(input(f"How many letters do you want? \n"))
# nr_symbols=int(input(f"How many symbols do you want? \n"))
# nr_numbers=int(input(f"How many numbers do you want \n"))

#easy version
# password=""
# for symbol in range(1, nr_symbols+1):
#     password+=random.choice(symbols)

# for number in range(1, nr_numbers+1):
#     password+=random.choice(numbers)

# for letter in range(1, nr_letters+1):
#     password+=random.choice(letters)

# print(f"Your password is {password}")

#hard version

# password_list=[]
# for symbol in range(1, nr_symbols+1):
#     password_list.append(random.choice(symbols))

# for number in range(1, nr_numbers+1):
#     password_list.append(random.choice(numbers))

# for letter in range(1, nr_letters+1):
#     password_list.append(random.choice(letters))

# print(password_list)
# random.shuffle(password_list)
# password=""
# for char in password_list:
#     password+=char

# print(f"Your password is {password}")