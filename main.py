from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(1000, 600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

l_paddle = Paddle(-450, 0)
r_paddle = Paddle(450, 0)
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()
    ball.move()

    # Detect collision with the wall
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    # Collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 430:
        ball.bounce_x()
    if ball.distance(l_paddle) < 50 and ball.xcor() < -430:
        ball.bounce_x()

    # Detect score
    if ball.xcor() > 480:
        ball.reset_position()
        score.l_point()

    if ball.xcor() < -480:
        ball.reset_position()
        score.r_point()


screen.exitonclick()
