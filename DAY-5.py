#DAY-5

# print("welcome to Average Height Calculator!")
# student_heights=input("Input a list student heights ").split()
# for n in range(0, len(student_heights)):
#     student_heights[n]=int(student_heights[n])
# print(student_heights)
# sum_height=0

# for height in student_heights:
#     sum_height+=height
# height_len=0
# for height in student_heights:
#     height_len+=1
# Average_Height= round(sum_height/height_len)
# print(f"Average Height is {Average_Height}")

# print("Welcome to the max result calculator!")
# student_result=input("input a list of student results ").split()

# for n in range(len(student_result)):
#     student_result[n]=int(student_result[n])

# high_score = student_result[0]
# for result in student_result:
#     if high_score < result:
#         high_score= result
# print(f"The highest score is {high_score}")

#Even sum between 1 and 100 including both 1 and 100
# first_num=1
# for number in range(1,11):
#     if number%2==0:
#         first_num+=number
# print(first_num)

# print("welcome to fizzbuzz game!")
# for number in range(1,101):
#     if number%3==0 and number%5==0:
#         print("fizzbuzz")
#     elif number%3==0:
#         print("Fizz")
#     elif number%5==0:
#         print("Buzz")
#     else:
#         print(number)


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






    






    









    
        
        
    












     




     

    

      










    

    
