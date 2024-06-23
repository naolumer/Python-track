from turtle import Turtle
import random

colors=["red","orange","yellow","green","blue","purple"]

STARTING_MOVE_POSITION= 5
MOVE_INCREMENT= 50



class Carmanager():
    
    def __init__(self):
        self.all_cars= []
        self.car_speed=STARTING_MOVE_POSITION
        
    def create_car(self):
        
        rand_chance= random.randint(1,6)
        if rand_chance==1:
            new_car= Turtle("square")
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.color(random.choice(colors))
            new_car.penup()
            random_y= random.randint(-250,250)
            new_car.goto(x=300,y=random_y)
            self.all_cars.append(new_car)
        
    def move_car(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_POSITION)
    
    def level_up(self):
        self.car_speed+=MOVE_INCREMENT
        
        
    