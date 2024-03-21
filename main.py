from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
screen= Screen()

screen.bgcolor("black")
screen.setup(width= 600, height= 600)
screen.title("snake_game")
screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.1)

    snake.move_snake()
    #detect collison with food
    if snake.snake_head.distance(food)< 15:
       snake.extend()
       scoreboard.increase_score()
       food.refresh()
    #detect collision with wall
    if snake.snake_head.xcor() >280 or snake.snake_head.xcor() <-280 or snake.snake_head.ycor() >280 or snake.snake_head.ycor() < -280:
        scoreboard.reset()
        snake.reset()
    #detect collision with own tail
    for segment in snake.segments[1:]:
        if snake.snake_head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
screen.exitonclick()