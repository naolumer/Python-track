# import turtle
# from turtle import Turtle, Screen
# timmy_the_turtle= Turtle()
# timmy_the_turtle.shape("turtle")
# turtle.colormode(255)
# import random

# for i in range(4):
#     timmy_the_turtle.forward(200)
#     timmy_the_turtle.right(90)
#     timmy_the_turtle.forward(200)
#     timmy_the_turtle.right(90)
#     timmy_the_turtle.forward(200)
#     timmy_the_turtle.right(90)
#     timmy_the_turtle.forward(200)

# for i in range(15):
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.pendown()

# tim= Turtle()
# tim.speed(0)
# colors = [
#     "black",
#     "white",
#     "red",
#     "green",
#     "blue",
#     "cyan",
#     "magenta",
#     "yellow",
#     "orange",
#     "purple",
#     "brown"
# ]

# def random_color():
#     r=random.randint(0,255)
#     g=random.randint(0,255)
#     b=random.randint(0,255)
#     random_colors= (r,g,b)
#     return random_colors


# def draw_polygon(num_sides):
#     angle= 360/num_sides
#     for i in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
        
# for i in range(3,10):
#     tim.color(random_color())
#     draw_polygon(i)

# rand_angles= [0,90,180,270]   
# tim.pensize(15)

# for i in range(300):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.right(random.choice(rand_angles))
# def draw_spirograph(gap_size):
#     for i in range(int(360/gap_size)):

#         tim.circle(100)
#         tim.color(random_color())
#         tim.setheading(tim.heading()+ gap_size)
        
# draw_spirograph(5)


# FINAL-PROJECT
# HIRST PAINTING

# import colorgram
# colors= colorgram.extract("20_001.jpg", 25)

# rgb_colors=[]
# for color in colors:
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b
#     new_color= (r,g,b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

# color_list= [(199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (222, 224, 227), (186, 158, 53), (6, 57, 83), (22, 122, 174), (64, 153, 138), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155), (179, 201, 186), (176, 198, 203)]
# import turtle
# from turtle import Turtle, Screen
# import random
# turtle.colormode(255)
# tim= Turtle()
# tim.penup()
# tim.hideturtle()
# tim.speed(0)
# tim.setheading(225)
# tim.forward(300)
# tim.setheading(0)
# number_of_dots=100


# for dot_counts in range(1, number_of_dots+1):
#     tim.dot(20, random.choice(color_list))
#     tim.forward(50)
#     if dot_counts%10==0:

#         tim.setheading(90)
#         tim.forward(50)
#         tim.setheading(180)
#         tim.forward(500)
#         tim.setheading(0)

# screen= Screen()
# screen.exitonclick()