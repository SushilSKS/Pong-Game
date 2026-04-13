from turtle import Screen
from paddle import Paddle
from ball import Ball
from time import sleep
from scoreboard import Score

screen = Screen()
screen.bgcolor("black")
screen.setup(1000, 700)
screen.title("Pong")
screen.tracer(0)

l_paddle = Paddle(-450, 0)
r_paddle = Paddle(450, 0)

l_paddle.l_control()
r_paddle.r_control()

ball = Ball()
score = Score()

is_game_on = True
while is_game_on:
    sleep(ball.ball_speed)
    screen.update()
    ball.move_ball()

    if ball.ycor() > 330 or ball.ycor() < -330:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 420 or ball.distance(l_paddle) < 50 and ball.xcor() < -420:
        ball.bounce_x()

    if ball.xcor() > 510:
        ball.reset_pos()
        score.update_l()

    if ball.xcor() < -510:
        ball.reset_pos()
        score.update_r()

screen.exitonclick()
