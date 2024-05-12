# Project: TURTLE RACING GAME USING TURTLE GRAPHICS


# from turtle import Turtle, Screen
# import random
# is_race_on= False
# screen= Screen()
# screen.setup(500,400)
# user_bet=screen.textinput(title="Make your bet", prompt= "Which turtle will win the race? Enter a color: ")
# colors=["red","pink","orange","blue","purple","green"]


# y_positions= [-70,-40,-10, 20, 50, 80]

# if user_bet:
#     is_race_on=True

# all_turtles=[]

# for turtle_index in range(0,6):
#     tim= Turtle(shape="turtle")
#     tim.color(colors[turtle_index])
#     tim.penup()
#     tim.goto(x=-230, y=y_positions[turtle_index])
#     all_turtles.append(tim)

# while is_race_on:
#     for turtle in all_turtles:
#         if turtle.xcor()> 225:
#             is_race_on=False
#             winning_color= turtle.pencolor()
#             if winning_color== user_bet:
#                 print(f"You've won. the winner is {winning_color} turtle.")
#             else:
#                 print(f"You've lost. the winner is {winning_color} turtle.")
        
#         random_distance=random.randint(0,10)
#         turtle.forward(random_distance)
    
    
    




# def move_forward():
#     tim.forward(10)
    
# def move_backward():
#     tim.backward(10)
# def turn_right():
#     new_heading= tim.heading() - 40
#     tim.setheading(new_heading)
# def turn_left():
#     new_heading= tim.heading() + 40
#     tim.setheading(new_heading)
# def clear():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
    
       


# screen.listen()
# screen.onkey(move_forward, "w")
# screen.onkey(move_backward, "s")
# screen.onkey(turn_right, "d")
# screen.onkey(turn_left, "a")
# screen.onkey(clear, "c")
# screen.exitonclick()