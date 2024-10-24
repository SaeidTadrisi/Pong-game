import time
from turtle import Screen

from paddle import Paddle
from ball import Ball
from score_board import ScoreBoard

screen = Screen()
screen.setup(height= 600, width= 800)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score_board = ScoreBoard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.ball_reset()
        score_board.right_increase_score()
        r_paddle.goto((350, 0))
        l_paddle.goto((-350, 0))

    if ball.xcor() < -380:
        ball.ball_reset()
        score_board.left_increase_score()
        r_paddle.goto((350, 0))
        l_paddle.goto((-350, 0))
screen.exitonclick()