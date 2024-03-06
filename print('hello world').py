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
# 
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
# result=4/2
# result/=2
# print(result)
# score=23
# height=1.6
# is_winning= True
# print(f"your score is {score}, and your height is {height}, and you winning is {is_winning}")


# print("welcome to week calculator!")
# age= input("what is your age \n")
# new_age=int(age)
# your_current_age= 90- new_age
# days_left= int(your_current_age)*365
# weeks_left=int(your_current_age)*52
# months_left= int(your_current_age)*12
# print(f"You have {days_left} days, {weeks_left} weeks and {months_left} months left")

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
# 
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
# else:
#     print("you have to grow to ride the rollercoaster")
#
# 
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
#     print(f"your score is {two_dig_number} , and you go tegether like coke and mentos")
# elif int(two_dig_number)>40 and int(two_dig_number)<50:
#     print(f"your score is {two_dig_number} , and you are perfect for each ohter ")
# else:
#     print(f"your score is {two_dig_number}")


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
# import random
# nub=random.randint(4,23)
# print(nub)
# fl_nub=random.random()
# print(fl_nub)
# bt=fl_nub* 5
# print(bt)

# print("welcome to heads or tails game!")
# toss_result= random.randint(0,1)
# if toss_result==0:
#     print("Heads")
# else:
#     print("Tails")
# import random
 
# print("welcome to the banker roulette!")
# name_string=input("Give me everybody's name separated by a coma.  \n ")
# name=name_string.split(",")
# num_item=len(name)
# rand_index= random.randint(0,num_item-1)
# rand_name = name[rand_index]
# print(f"{rand_name} should pay the bill")
# list=["elias", "dolphin", "mahamed"]
# additional=list.append("naol")
# print(list)
# list[0]="Elias"
# print(list)


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

print("welcome to Average Height Calculator!")
student_heights=input("Input a list student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n]=int(student_heights[n])
print(student_heights)
sum_height=0
for height in student_heights:
    sum_height+=height
height_len=0
for height in student_heights:
    height_len+=1
Average_Height= round(sum_height/height_len)
print(f"Average Height is {Average_Height}")
    






    









    
        
        
    












     




     

    

      










    

    
