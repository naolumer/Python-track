#DAY-1

# INTRO TO PYTHON
# print("hello world")
# numb=5+5
# print(numb)
# numb=5/2
# print(numb)
# numb=9%2
# print(numb)
# my_numb=5
# my_numb+=5
# print(my_numb)
# def add(n1,n2):
#     print(n1+n2)
# add(3,3)
# add(5,6)
# def my_function():
#     print("hello")
#     name=input("what is your name: ")
#     print("hello", name)
# my_function()
# my_function()
# def addd(n1, n2):
#     return n1 + n2
# result= addd(2, 3)
# addd()
# print(result)
# addd()
# solution = addd(4, 5)
# print(solution)
# result=addd(2,8)
# print(result)
# def divide(n1, n2):
#     result= n1/n2
#     print(result)
# divide(3,2) 
# divide(5,1)
# divide(9,2)
# # n=2
# def my_function():
#     n=3
#     print(n)
# my_function()
# n=5
# if n>5:
#     print("true")
# else:
#     print("not true")
# age=16
# if age>18:
#     print("You can drive")
# else:
#     print("Under Age")
# weather= "sunny"
# if weather=="rainy":
#     print("bring an umbrella")
# elif weather=="sunny":
#     print("bring your sunglasses")
# elif weather=="snow":
#     print("bring gloves")
# S=56
# if S>50 and S<70:
#     print("your grade is B")
# age=13
# if age>12 or age<8:
#     print("you can't drive")
# if not 4>5:
#     print("wrong")
# age= 13
# if age!=12:
#     print("not suitable for the job")
# elif age>12:
#     print("Good Condition")
# n=12
# while n<25:
#     n+=1
#     print(n)
# scores=[24, 45, 67, 98, 105]
# for s in scores:
#     if s>10:
#         print(s)
# n=0
# while n<50:
#     n+=1
#     if n%2==0:
#         print(n)
# n=1
# while n<40:
#     n+=2
#     if n%2==0:
#         continue
#     print(n)
# list_1= [23,35,67,78]
# list_2= [45,78,44,77]
# new_list= list_1 + list_2
# print(new_list)
# all_fruit=["applea", "bannana", "orange"]
# all_fruit.append("pear")
# print(all_fruit)
# letters= ["a", "b","c","d","e","f"]
# print(letters[0,2])
# print(letters[-1:])
# for i in range(6, 0, -2) :
#     print(i)
# import random
# n=random.randint(2,9)
# numb=round(5.5)
# print(numb)
# import random as r
# n=r.randint(2,5)
# print(n)
# print("day-1 pyhton print function")
# print("print('what to print')")
# print("the function is executed like this: ")
# print("Hello world!\nHello world!\nHello world!\nHello world!")
# input("what is your name: ")
# print("Hello "+ input("what is your name: ")+ "!")
# #input is first executed then followed by hello and exclamation mark
# name=input("what is your name: ")
# number_of_letters=len(name)
# print(number_of_letters)
# print(len(input("what is your name? ")))
# a= input("a: ")
# b= input("b: ")
# c= a
# a= b
# b= c
# print("a= " + a)
# print("b= " + b)
# 
# print("welcome to the band name generator!.")
# city=input("what is the city you were born in? ")
# pet=input("what is the name of your pet? ")
# print("Your band name is: " + city + pet)
# print(len("naol"))
# print("Hello"[1])
# num_chart=(len(input("what is your name: ")))
# new_numchart=str(num_chart)
# print("your name has " + new_numchart + " "+ "number of characters")
# two_digit_number= input("type a two digit number: ")
# remainder = two_digit_number[0]
# quotient = two_digit_number[1]
# print(remainder, quotient)
# print(int(remainder)+ int(quotient))
# print(float(13))
# print(3+3)
# print(3*3)
# print(3/1)
# print(3**2)

# DAY-2

# BMI CALCULATOR TOOL

# print("welcome to BMI calculator tool!")
# height=input("What is your height: \n")
# weight=input("What is your weight: \n")
# BMI = float(weight)/(float(height))**2
# new_BMI= str(BMI)
# if BMI < 18.5:
#     print("your BMI is " + new_BMI + " and you are under weight")
# elif BMI > 18.5 and BMI<25:
#     print("your BMI is " + new_BMI + " and you are normal")
# elif BMI > 25 and BMI< 30:
#     print("your BMI is " + new_BMI + " and you are overweight")
# elif BMI > 30:
#     print("your BMI is " + new_BMI + " and you are Obese")

# WEEK CALCULATOR

# print("welcome to week calculator!")
# age= input("what is your age \n")
# new_age=int(age)
# your_current_age= 90- new_age
# days_left= int(your_current_age)*365
# weeks_left=int(your_current_age)*52
# months_left= int(your_current_age)*12
# print(f"You have {days_left} days, {weeks_left} weeks and {months_left} months left")

# TIP CALCULATOR

# print("welcome to the tip calculator!")
# total_bill=input("What is the total bill? \n")
# tip_percentage= input("What percentage tip would you like to pay?" + " 10, 12, or 15 ?")
# intig_of_tip_percentage=int(tip_percentage)
# no_of_people=input("how many people to split the bill?\n")
# ten_percent_tip= (int(tip_percentage)/100)*float(total_bill)
# twelve_percent_tip=(int(tip_percentage)/100)*float(total_bill)
# fifteen_percent_tip=(int(tip_percentage)/100)*float(total_bill)
# if intig_of_tip_percentage== 12:
#     print(f"Each person should pay   {(int(total_bill)/int(no_of_people)) + (twelve_percent_tip/int(no_of_people))}  birr")
# elif intig_of_tip_percentage==10:
#     print(f"Each person should pay   {(int(total_bill)/int(no_of_people)) + (ten_percent_tip/int(no_of_people))}  birr")
# elif intig_of_tip_percentage==15:
#     print(f"Each person should pay   {(int(total_bill)/int(no_of_people)) + (fifteen_percent_tip/int(no_of_people))}  birr")
# print("welcome to bill calculator!")
# bill=float(input("what is the total bill? $"))
# tip= int(input("what percentage tip would you like to pay? 10, 12, or 15 ?"))
# people=int(input("how many people to split the bill? "))
# tip_amount=tip/100 * bill
# total_amount=bill + tip_amount
# amount_per_person=round(total_amount/people, 2)
# amount_per_person="{:.2f}".format(total_amount/people)
# print(f"Each person should pay  ${amount_per_person}")

# ROLLER COASTER

# print("welcome to the rollercoaster !")
# height=int(input("what is your height is cm ? "))
# if height>180:
#     print("you can ride the rollercoaster")
# else:
#     print("you have to grow in height before you can ride the rollercoaster")
# b=0
# height=int(input("what is your height in cm ? "))
# if height>120:
#     print("you can ride the rollercoaster")
#     age=int(input("what is your age?"))
#     if age<12:
#         bill=5
#         print("you should pay $5")
#     elif age<=18:
#         bill=7
#         print("you shoukd pay $7")
#     elif age>45 and age<55:
#         bill=0
#         print("you can ride for free")
#     else:
#         bill=12
#         print("Please pay $12")
#     wants_photo= input( "do you want a photo ? yes or no " )
#     if wants_photo=="yes":
#         bill+=3
#         print(f"your have to pay ${bill} ")
#     if wants_photo=="no":
#         bill+=0
#         print(f"your final bill is ${bill}")

# DAY-3

# LEAP YEAR CHECKER

# print("welcome to leap year checker!")
# year=int(input("Which year would you like to check: "))
# if year%4==0:
#     if year%100==0:
#         if year%400==0:
#             print("leap year");
#         else:
#             print("not leap year")
#     else:
#         print("leap year")
# else:
#     print("not leap year")


# PYTHON PIZZA PROGRAM

# bill=0
# print("Welcome to python pizza!")
# size=input("what size do you want? S, M or L ?")
# add_pepperoni=input("do you want pepperoni? Y or N ?")
# extra_cheese=input("do you want extra cheese? Y or N ?")
# if size=="S":
#     bill+=15
# elif size=="M":
#     bill+=20
# else:
#     bill+=25
# if add_pepperoni=="Y":
#     if size=="S":
#         bill+=2
#     else:
#         bill+=3
# if extra_cheese=="Y":
#     bill+=1
# print(f"your final bill is ${bill}")

# LOVE CALCULATOR

# print("Welcome to the love calculator!")
# name_1=input("what is your name? \n")
# name_2=input("what is their name? \n")
# ln1=name_1.lower()
# ln2=name_2.lower()
# tn1=int(ln1.count("t"))
# tn2=int(ln2.count("t"))
# rn1=int(ln1.count("r"))
# rn2=int(ln2.count("r"))
# un1=int(ln1.count("u"))
# un2=int(ln2.count("u"))
# en1=int(ln1.count("e"))
# en2=int(ln2.count("e"))
# lln1=int(ln1.count("l"))
# lln2=int(ln2.count("l"))
# on1=int(ln1.count("o"))
# on2=int(ln2.count("o"))
# vn1=int(ln1.count("v"))
# vn2=int(ln2.count("v"))
# len1=int(ln1.count("e"))
# len2=int(ln2.count("e"))
# for_true= tn1+tn2+rn1+rn2+un1+un2+en1+en2
# for_love= lln1+lln2+on1+on2+vn1+vn2+len1+len2
# two_dig_number=str(for_true) + str(for_love)

# if int(two_dig_number)<10 or int(two_dig_number)>90:
#     print(f"your score is {two_dig_number} , and you go together like coke and mentos")
# elif int(two_dig_number)>40 and int(two_dig_number)<50:
#     print(f"your score is {two_dig_number} , and you are perfect for each other ")
# else:
#     print(f"your score is {two_dig_number}")

# TREASURE ISLAND GAME

# print("Welcome to treasure island!")
# print("Your mission is to find the treasure")
# direction=input("You are at a cross road. Where do you wanna go? right or left? \n")
# if direction == "right":
#     print("You entered a Hole. Game Over!")
# if direction=="left":
#     swim_or_wait=input("You come to a lake. There is an island in the middle of the lake, type 'SWIM'to swim and type 'WAIT' to wait for a boat \n")
#     if swim_or_wait=="SWIM":
#         print("You have entered a lake full of crocodiles. Game Over!")
#     if swim_or_wait=="WAIT":
#         color= input("You have arrived at the island.There is a house with 3 doors. Red, Yellow, and Blue. which color do you choose? \n")
#         if color== "Red" or color=="Blue":
#             print("You entered a house full of snakes, Game Over!")
#         elif color=="Yellow":
#             print("You have found the treasure, Congratulations!")



#DAY-4

# HEADS OR TAILS

# print("welcome to heads or tails game!")
# import random
# toss_result= random.randint(0,1)
# if toss_result==0:
#     print("Heads")
# else:
#     print("Tails")

# BANKER ROULETTE

# import random
# print("welcome to the banker roulette!")
# name_string=input("Give me everybody's name separated by a coma.  \n ")
# name=name_string.split(",")
# num_item=len(name)
# rand_index= random.randint(0,num_item-1)
# rand_name = name[rand_index]
# print(f"{rand_name} should pay the bill")


# TREASURE MAP

# print("welcome to treasure Map!")
# row1=["⏹","⏹","⏹"]
# row2=["⏹","⏹","⏹"]
# row3=["⏹","⏹","⏹"]
# map=[row1,row2,row3]
# print(f"{row1}\n{row2}\n{row3}")
# position=input("Where do you want to put the treasure? ")
# horizontal=int(position[0])
# vertical=int(position[1])
# selected_row=map[vertical-1]
# selected_row[horizontal-1]="X"
# print(f"{row1}\n{row2}\n{row3}")

# PROJECT: ROCK, PAPER, SCISSORS

# print("welcome to rock paper scissors Game!")
# choice=input("What do you choose ? Type 0 for Rock, 1 for paper and 2 for scissors. ")
# rock="🪨"
# paper="📃"
# scissors="✂️"
# if choice=="0":
#     print("You have chosen " + rock)
# elif choice=="1":
#     print("You have chosen " + paper)
# elif choice=="2":
#     print("You have chosen " + scissors)

# import random
# choice_int=int(choice)
# random_pic=random.randint(0,2)
# if random_pic==0 and choice=="0":
#     print("and the computer has chosen " + rock + "  So, it is a DRAW!")
# elif random_pic==0 and choice=="2":
#     print("and the computer has chosen " + rock + "  So, You Lost, 🙃 !")
# elif random_pic==0 and choice=="1":
#     print("and the computer has chosen " + rock + "  So, You Have Won, Congrats!")
# elif random_pic==1 and choice=="1":
#     print("and the computer has chosen " + paper + "  So, it is a DRAW!")
# elif random_pic==1 and choice=="0":
#     print("and the computer has chosen " + paper + "  So, You Lost, 🙃!")
# elif random_pic==1 and choice=="2":
#     print("and the computer has chosen " + paper + "  So, You Have Won, Congrats!")
# elif random_pic==2 and choice=="0":
#     print("and the computer has chosen " + scissors + "  So, You Have Won, Congrats!")
# elif random_pic==2 and choice=="1":
#     print("and the computer has chosen " + scissors + "  So, You Lost, 🙃!")
# elif random_pic==2 and choice=="2":
#     print("and the computer has chosen " + scissors + "  So, it is a DRAW!")
# else:
#     print("Invalid input⛔️")

# fruits=["apple", "banana", "pears"]
# for fruit in fruits:
#     print(fruit + " pie")

#DAY-5

# AVE HEIGHT CALCULATOR

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

# MAX RESULT CALCULATOR

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

# FIZZBUZZ
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

#DAY-6
#final project maze done online 


#DAY-7
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

# DAY-8

#FUNCTIONS WITH INPUTS

# def greet():
#     print("""Hello
# hi
# adios""")
    
# greet()

# #functions with inputs
# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}")   

# greet_with_name("Naol")
# greet_with_name("Imran")
#functions with multiple inputs
# def salute(namee, location):
#     print(f"Hello {namee}")
#     print(f"What is it like in {location}")
# salute("Naol", "Adama")


# PAINT AREA CALCULATOR

#print("welcome to paint area calculator")
# import math
# def paint_calculator(width, height, coverage):
#     no_of_can=math.ceil((width*height)/5)
#     print(f"You need to buy {no_of_can} cans")
# wid=int(input("enter the width: "))
# hei=int(input("enter the height"))
# cover=5
# paint_calculator(width=wid,height=hei,coverage=cover)

#PRIME NUMBER CHECKER

#print("welcome to prime number checker!")
# def prime_num_checker(number):
#     if int(number)==0 or int(number)==1:
#         print("not prime")

#     else:
#         counter=0
#         for i in range(1,number):
#             if number%i==0:
#                 counter+=1
#         # print(counter)
#         if counter==1:
#             print("prime")
#         else:
#             print("not prime")

    
# n=int(input("enter the number you want to check: "))
# prime_num_checker(number=n)


# PROJECT: CAESAR CIPHER ENCRYPTION

# print("welcome to CESAR CIPHER ENCRYPTION")
# should_continue= True
# while should_continue:


#     alphabet=['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#     direction=input("Type 'encode' to encrypt and 'decode' to decrypt \n")
#     text=input("What is your message: \n").lower()
#     shift= int(input("What is your shift: \n"))
#     shift= shift%26


# two function with if else
# def encode(text, shift):
#     cipher_text=""
#     for position in range(len(text)):

#         letter=ord(text[position]) - 96
#         shift= shift%26
#         new_letter= letter + shift
#         new_leter= alphabet[new_letter-1]
#         cipher_text+= new_leter
#     print(f"The ciphered text is '{cipher_text}' ")

# encode(text, shift)

# def decode(text, shift):
#    plain_text=""
#    for position in range(len(text)):
#       letter= ord(text[position])-96
#       shift= shift%26
#       new_letter= letter - shift
#       new_leter= alphabet[new_letter-1]
#       plain_text+=new_leter

      
#    print(f"the plain text is '{plain_text}' ")

# decode(text, shift)
# if direction == "encode":
#    encode(text, shift)
# elif direction =="decode":
#    decode(text, shift)
# else:
#    print("invalid input")

# single function method
    # def cesar(start_text, shift_amount, caesar_direction):
    #     end_text=""
    #     if caesar_direction== "decode":
    #         shift_amount*=-1
    #     for char in start_text:
    #         if char in alphabet:
    #            position= alphabet.index(char)
    #            new_position= position + shift_amount
    #            end_text+= alphabet[new_position]
    #         else:
    #             end_text+= char
    #     print(f"the {caesar_direction}d text is {end_text}")

    # cesar(start_text=text, shift_amount=shift, caesar_direction=direction)
    # result= input("If you want to continue type 'yes' otherwise type 'no': \n")
    # if result=="no":
    #     should_continue= False
    #     print("Goodbye")

# DAY-9
#DICTIONARIES AND NESTED LISTS

# programming_dictionary= {"Bug": "an error in a program that prevents it from working as expected.",
#                          "Function": "a piece of code that you can call it again and again.",
#                           "Loop": "the action of doing something over and over again.", }
# print(programming_dictionary["Bug"])
# programming_dictionary["Bug"]= " A moth in your computer. "
# print(programming_dictionary)
# for keys in programming_dictionary:
#     print(programming_dictionary[keys])

# coding exercise

# GRADE CALCULATER

# print("Welcome to grade calculator")
# student_scores={"Harry": 81,"Ron": 78, "Hermione": 99, "Draco":74, "Neville": 62, }
# student_grades={}
# for students in student_scores:
#     score=student_scores[students]
#     if score>90:
#         student_grades[students]= "Outstanding"
#     elif score>80:
#         student_grades[students]= "Exceeds expectations"
#     elif score>70:
#         student_grades[students]= "Acceptable"
#     elif score>60:
#         student_grades[students]= "Failed"
# print(student_grades)

# travel_log= [{"country": "France", 
#               "visits": 12,
#               "cities":["lille", "paris", "dijon"],},
#               {"country": "germany",
#                "visits":5,
#                "cities": ["berlin","hamburg","stuttgart"]},]
#coding exercise; dictionaries in list
# def add_country(country, visits, cities):
#     new_country ={}
#     new_country["country"]= country
#     new_country["visits"]= visits
#     new_country["cities"]= cities
#     travel_log.append(new_country)
# add_country("ethiopia", 3, ["adama", "bishoftu", "hawasa"])
# print(travel_log)


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

#DAY-10
# FUNCTIONS WITH OUTPUTS

# def format_name(f_name, l_name):
#     format_name_f= f_name.title()
#     format_name_l= l_name.title()
#     return f"{format_name_f} {format_name_l}"  
# print(format_name("naol", "uMEr") )  

# PROJECT: CALCULATOR

# def add(a1, a2):
#     return a1 + a2
# def subtract(a1, a2):
#     return a1 - a2
# def multiply(a1, a2):
#     return a1 * a2
# def divide(a1, a2):
#     return a1/a2

# operations= {"+": add, "-": subtract, "*": multiply, "/": divide}
# def calculator():
#     num1= float(input("what is the first number? \n"))
#     for keys in operations:
#         print(keys)

#     stop_operation= False
#     while not stop_operation:
#         operation_symbol= input("pick an operation \n")
#         num2= float(input("what's the next number? \n"))
#         calc_operation= operations[operation_symbol]
#         answer= calc_operation(num1, num2)
#         print(f"{num1} {operation_symbol} {num2} = {answer}")
#         should_continue= input(f"type 'y' to do further operations with {answer} or type 'n' to restart calculator \n ")
#         if should_continue== "y":
#             num1=answer
#         elif should_continue=="n":
#             stop_operation= True
#             calculator()
# calculator()

# Day-11
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

# DAY-12
#SCOPE: LOCAL VS GLOBAL
# value= 5
# def dsfsg():
#     nvalue= value
#     print(nvalue)
#     nvalue+=12
#     print(nvalue)
# dsfsg()

# def add(num1, num2):
#     total= num1+num2
#     print( total)
# add(2,5)


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

# DAY-13 (DEBUGGING)

# import random
# num= random.randint(1,6)   
# print(num)

# pages= 0
# words_per_page=0
# pages= int(input("number of pages: "))
# words_per_page=int(input("number of words per page: "))
# total_words=pages* words_per_page
# print(total_words)

# Leap_year_checker
# year= int(input("what year would you like to check? :"))
# if year%4==0:
#     if year%100==0:
#         if year%400==0:
#             print("leap year")
#         else:
#             print("not leap year")
#     else:
#         print("leap year")
# else:
#     print("not leap year")        

# for number in range(1,101):
#     if number%3==0 and number%5==0:
#         print("FizzBuzz")
#     elif number%3==0:
#         print("Fizz")
#     elif number%5==0:
#         print("Buzz")
#     else:
#         print(number)

#DAY-14
# PROJECT: HIGHER OR LOWER GAME

# # import random
# # vs = """
# #  _    __    
# # | |  / /____
# # | | / / ___/
# # | |/ (__  ) 
# # |___/____(_)
# # """
# # logo = """
# #     __  ___       __             
# #    / / / (_)___ _/ /_  ___  _____
# #   / /_/ / / __ `/ __ \/ _ \/ ___/
# #  / __  / / /_/ / / / /  __/ /    
# # /_/ ///_/\__, /_/ /_/\___/_/     
# #    / /  /____/_      _____  _____
# #   / /   / __ \ | /| / / _ \/ ___/
# #  / /___/ /_/ / |/ |/ /  __/ /    
# # /_____/\____/|__/|__/\___/_/     
# # """
# data = [
#     {
#         'name': 'Instagram',
#         'follower_count': 346,
#         'description': 'Social media platform',
#         'country': 'United States'
#     },
#     {
#         'name': 'Cristiano Ronaldo',
#         'follower_count': 215,
#         'description': 'Footballer',
#         'country': 'Portugal'
#     },
#     {
#         'name': 'Ariana Grande',
#         'follower_count': 183,
#         'description': 'Musician and actress',
#         'country': 'United States'
#     },
#     {
#         'name': 'Dwayne Johnson',
#         'follower_count': 181,
#         'description': 'Actor and professional wrestler',
#         'country': 'United States'
#     },
#     {
#         'name': 'Selena Gomez',
#         'follower_count': 174,
#         'description': 'Musician and actress',
#         'country': 'United States'
#     },
#     {
#         'name': 'Kylie Jenner',
#         'follower_count': 172,
#         'description': 'Reality TV personality and businesswoman and Self-Made Billionaire',
#         'country': 'United States'
#     },
#     {
#         'name': 'Kim Kardashian',
#         'follower_count': 167,
#         'description': 'Reality TV personality and businesswoman',
#         'country': 'United States'
#     },
#     {
#         'name': 'Lionel Messi',
#         'follower_count': 149,
#         'description': 'Footballer',
#         'country': 'Argentina'
#     },
#     {
#         'name': 'Beyoncé',
#         'follower_count': 145,
#         'description': 'Musician',
#         'country': 'United States'
#     },
#     {
#         'name': 'Neymar',
#         'follower_count': 138,
#         'description': 'Footballer',
#         'country': 'Brasil'
#     },
#     {
#         'name': 'National Geographic',
#         'follower_count': 135,
#         'description': 'Magazine',
#         'country': 'United States'
#     },
#     {
#         'name': 'Justin Bieber',
#         'follower_count': 133,
#         'description': 'Musician',
#         'country': 'Canada'
#     },
#     {
#         'name': 'Taylor Swift',
#         'follower_count': 131,
#         'description': 'Musician',
#         'country': 'United States'
#     },
#     {
#         'name': 'Kendall Jenner',
#         'follower_count': 127,
#         'description': 'Reality TV personality and Model',
#         'country': 'United States'
#     },
#     {
#         'name': 'Jennifer Lopez',
#         'follower_count': 119,
#         'description': 'Musician and actress',
#         'country': 'United States'
#     },
#     {
#         'name': 'Nicki Minaj',
#         'follower_count': 113,
#         'description': 'Musician',
#         'country': 'Trinidad and Tobago'
#     },
#     {
#         'name': 'Nike',
#         'follower_count': 109,
#         'description': 'Sportswear multinational',
#         'country': 'United States'
#     },
#     {
#         'name': 'Khloé Kardashian',
#         'follower_count': 108,
#         'description': 'Reality TV personality and businesswoman',
#         'country': 'United States'
#     },
#     {
#         'name': 'Miley Cyrus',
#         'follower_count': 107,
#         'description': 'Musician and actress',
#         'country': 'United States'
#     },
#     {
#         'name': 'Katy Perry',
#         'follower_count': 94,
#         'description': 'Musician',
#         'country': 'United States'
#     },
#     {
#         'name': 'Kourtney Kardashian',
#         'follower_count': 90,
#         'description': 'Reality TV personality',
#         'country': 'United States'
#     },
#     {
#         'name': 'Kevin Hart',
#         'follower_count': 89,
#         'description': 'Comedian and actor',
#         'country': 'United States'
#     },
#     {
#         'name': 'Ellen DeGeneres',
#         'follower_count': 87,
#         'description': 'Comedian',
#         'country': 'United States'
#     },
#     {
#         'name': 'Real Madrid CF',
#         'follower_count': 86,
#         'description': 'Football club',
#         'country': 'Spain'
#     },
#     {
#         'name': 'FC Barcelona',
#         'follower_count': 85,
#         'description': 'Football club',
#         'country': 'Spain'
#     },
#     {
#         'name': 'Rihanna',
#         'follower_count': 81,
#         'description': 'Musician and businesswoman',
#         'country': 'Barbados'
#     },
#     {
#         'name': 'Demi Lovato',
#         'follower_count': 80,
#         'description': 'Musician and actress',
#         'country': 'United States'
#     },
#     {
#         'name': "Victoria's Secret",
#         'follower_count': 69,
#         'description': 'Lingerie brand',
#         'country': 'United States'
#     },
#     {
#         'name': 'Zendaya',
#         'follower_count': 68,
#         'description': 'Actress and musician',
#         'country': 'United States'
#     },
#     {
#         'name': 'Shakira',
#         'follower_count': 66,
#         'description': 'Musician',
#         'country': 'Colombia'
#     },
#     {
#         'name': 'Drake',
#         'follower_count': 65,
#         'description': 'Musician',
#         'country': 'Canada'
#     },
#     {
#         'name': 'Chris Brown',
#         'follower_count': 64,
#         'description': 'Musician',
#         'country': 'United States'
#     },
#     {
#         'name': 'LeBron James',
#         'follower_count': 63,
#         'description': 'Basketball player',
#         'country': 'United States'
#     },
#     {
#         'name': 'Vin Diesel',
#         'follower_count': 62,
#         'description': 'Actor',
#         'country': 'United States'
#     },
#     {
#         'name': 'Cardi B',
#         'follower_count': 67,
#         'description': 'Musician',
#         'country': 'United States'
#     },
#     {
#         'name': 'David Beckham',
#         'follower_count': 82,
#         'description': 'Footballer',
#         'country': 'United Kingdom'
#     },
#     {
#         'name': 'Billie Eilish',
#         'follower_count': 61,
#         'description': 'Musician',
#         'country': 'United States'
#     },
#     {
#         'name': 'Justin Timberlake',
#         'follower_count': 59,
#         'description': 'Musician and actor',
#         'country': 'United States'
#     },
#     {
#         'name': 'UEFA Champions League',
#         'follower_count': 58,
#         'description': 'Club football competition',
#         'country': 'Europe'
#     },
#     {
#         'name': 'NASA',
#         'follower_count': 56,
#         'description': 'Space agency',
#         'country': 'United States'
#     },
#     {
#         'name': 'Emma Watson',
#         'follower_count': 56,
#         'description': 'Actress',
#         'country': 'United Kingdom'
#     },
#     {
#         'name': 'Shawn Mendes',
#         'follower_count': 57,
#         'description': 'Musician',
#         'country': 'Canada'
#     },
#     {
#         'name': 'Virat Kohli',
#         'follower_count': 55,
#         'description': 'Cricketer',
#         'country': 'India'
#     },
#     {
#         'name': 'Gigi Hadid',
#         'follower_count': 54,
#         'description': 'Model',
#         'country': 'United States'
#     },
#     {
#         'name': 'Priyanka Chopra Jonas',
#         'follower_count': 53,
#         'description': 'Actress and musician',
#         'country': 'India'
#     },
#     {
#         'name': '9GAG',
#         'follower_count': 52,
#         'description': 'Social media platform',
#         'country': 'China'
#     },
#     {
#         'name': 'Ronaldinho',
#         'follower_count': 51,
#         'description': 'Footballer',
#         'country': 'Brasil'
#     },
#     {
#         'name': 'Maluma',
#         'follower_count': 50,
#         'description': 'Musician',
#         'country': 'Colombia'
#     },
#     {
#         'name': 'Camila Cabello',
#         'follower_count': 49,
#         'description': 'Musician',
#         'country': 'Cuba'
#     },
#     {
#         'name': 'NBA',
#         'follower_count': 47,
#         'description': 'Club Basketball Competition',
#         'country': 'United States'
#     }
# ]


# # def format_account(account):
# #     name= account["name"]
# #     description= account["description"]
#     country= account["country"]
#     return f"{name},a {description}, from {country}"
# def check_answer(guess, a_follower, b_follower):
#     if a_follower>b_follower:
#         return guess=="a"
#     else:
#         return guess=="b"
# should_continue=True
# score=0
# account_b= random.choice(data)
# while should_continue:
#     account_a= account_b
#     account_b= random.choice(data)
#     if account_a==account_b:
#         account_b= random.choice(data)
#     print(logo)

#     print(f"compare A: {format_account(account_a)}")
#     print(vs)
#     print(f"Against B: {format_account(account_b)}")

#     guess= input("Who has more followers? Type 'A' or 'B' : ")
#     a_follower= account_a["follower_count"]
#     b_follower= account_b["follower_count"]

#     is_correct= check_answer(guess, a_follower, b_follower)
#     if is_correct:
#         score+=1
#         print(f"You are right and your score is: {score}")

#     else:
#         should_continue= False
#         print(f"Sorry, Thats wrong, Final score: {score}")

# DAY-15

# PROJECT: COFFEE MACHINE
# MENU = {
#     "espresso": {
#         "ingredients": {
#             "water": 50,
#             "coffee": 18,
#         },
#         "cost": 1.5,
#     },
#     "latte": {
#         "ingredients": {
#             "water": 200,
#             "milk": 150,
#             "coffee": 24,
#         },
#         "cost": 2.5,
#     },
#     "cappuccino": {
#         "ingredients": {
#             "water": 250,
#             "milk": 100,
#             "coffee": 24,
#         },
#         "cost": 3.0,
#     }
# }




# profit = 0
# resources = {
#     "water": 300,
#     "milk": 200,
#     "coffee": 100,
# }
# def is_resource_sufficient(order_ingredients):
#     for item in order_ingredients:
#         if order_ingredients[item]>=resources[item]:
#             print(f"Sorry, there isn't enough {item}")
#             return False
#     return True

# def process_coins():
#     print("Please insert coins:")
#     total= int(input("How many pennies?: "))*0.01
#     total+= int(input("How many dimes ?: "))*0.1
#     total+= int(input("How many nickles?: "))*0.05
#     total+= int(input("How many quarters?: "))*0.25
#     return total

# def is_transaction_successful(money_paid, drink_cost ):
#     if money_paid>=drink_cost:
#         change= round(money_paid-drink_cost, 2)
#         print(f"Here is ${change} in change.")
#         global profit
#         profit+=drink_cost
#         return True
#     else:
#         print("Sorry, that's not enough money")
#         return False

# def make_coffee(drink_name, order_ingredients):
#     for item in order_ingredients:
#         resources[item]-=order_ingredients[item]
#     print(f"Here is your {drink_name}☕.enjoy! ")

# end_of_game= False
# while not end_of_game:
#     choice= input("What would you like? espresso/latte/cappuccino: ").lower()
#     if choice=="off":
#         end_of_game=True
#     elif choice=="report":
#         print(f"water: {resources['water']}ml")
#         print(f"milk: {resources['milk']}ml")
#         print(f"coffee: {resources['coffee']}g")
#         print(f"money:${profit}")
#     else:
#         drink= MENU[choice]
#         if is_resource_sufficient(drink["ingredients"]):
#             payment=process_coins()
            
#             if is_transaction_successful(payment,drink["cost"]):
#                 make_coffee(choice, drink["ingredients"])
            
# PALINDROME CHECKER

# user_input= input("your text(without any space): ").lower()
# counter= len(user_input)
# reversed_word= ""
# for char in user_input:
#     counter-=1
#     char= user_input[counter]
#     reversed_word+=char
#     if reversed_word==user_input:
#         condition="palindrome"
#     else:
#         condition="Not palindrome"
# print(condition)
