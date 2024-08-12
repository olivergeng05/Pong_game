from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

paddle1 = Paddle(350)
paddle2 = Paddle(-350)
ball = Ball()


screen = Screen()
screen.tracer(0)
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('pong')
screen.listen()


screen.onkey(paddle1.move_up, 'Up')
screen.onkey(paddle1.move_down, 'Down')
screen.onkey(paddle2.move_up, 'w')
screen.onkey(paddle2.move_down, 's')

game_on = True
scoreboard = Scoreboard()

while game_on:
    time.sleep(ball.move_speed)
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.distance(paddle1) < 50 and ball.xcor() > 320 or ball.distance(paddle2) < 50 and ball.xcor() < -320:
        ball.collide()

    if ball.xcor() > 400:
        ball.goto(0,0)
        ball.x_move *= -1
        ball.move_speed = .1
        scoreboard.left_up()

    if ball.xcor() < -400:
        ball.goto(0,0)
        ball.x_move *= -1
        ball.move_speed = .1
        scoreboard.right_up()

    screen.update()

screen.exitonclick()