import time
from snake import Snake
from turtle import Screen
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SNAKE")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
sleep_time = 0.1

while game_is_on:
    screen.update()
    time.sleep(sleep_time)
    snake.move()

    # Detect collision w/ food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        sleep_time = snake.increase_speed(sleep_time)
        scoreboard.increase_score()

    # Detect collision w/ wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()
        sleep_time = 0.1

    # Detect collision w/ tail
    for segment in snake.turtle_segments[3:]:
        if snake.head.distance(segment) < 5:
            scoreboard.reset()
            snake.reset()
            sleep_time = 0.1

screen.exitonclick()
