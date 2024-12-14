from turtle import *
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(width = 800,height = 600)
screen.title("Pong")
screen.tracer(0)

r_pad = Paddle(350,0)
l_pad = Paddle(-360,0)

ball = Ball()
l_score = ScoreBoard(-150,200)
r_score = ScoreBoard(150,200)
screen.listen()
screen.onkey(key ="Up",fun = r_pad.up)
screen.onkey(key ="Down",fun = r_pad.down)
screen.onkey(key ="w",fun = l_pad.up)
screen.onkey(key ="s",fun = l_pad.down)


game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #collision detection with r_paddle
    if (ball.distance(r_pad) < 50 and ball.xcor() >330) or (ball.distance(l_pad) < 50 and ball.xcor() < -330) :
        ball.bounce_x()


    if ball.xcor() > 380 :
        ball.refresh()
        l_score.l_update_score()

    if ball.xcor() < -380 :
        ball.refresh()
        r_score.r_update_score()

screen.exitonclick()