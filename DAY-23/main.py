import time
from player import Player
from scoreboard import Scoreboard
from turtle import Turtle, Screen
from car_manager import Carmanager

player= Player()
carmanager= Carmanager()
scoreboard= Scoreboard()

screen= Screen()
screen.setup(width=600,height=600)
screen.tracer(0)

screen.listen()
screen.onkey(player.go_up, "Up")



is_game_on= True
while  is_game_on:
    time.sleep(0.1)
    screen.update()
    
    carmanager.create_car()
    carmanager.move_car()
    
    # detect collision with a car
    for car in carmanager.all_cars:
        if car.distance(player)<20:
            is_game_on=False
            scoreboard.game_over()
            
    
    # detect successful_crossing
        if player.is_at_finish_line():
            player.goto_start()
            carmanager.level_up()
            scoreboard.increase_level()
    
screen.exitonclick()
    
    
    