from turtle import Screen
from paddles import Paddle
from ball import Ball
from scoreboard import Scoreboard
from center_line import DottedLine
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("PONG")
screen.tracer(0)

p1 = Paddle((350, 0))
p2 = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
center_line = DottedLine()
center_line.draw_line()

screen.listen()
screen.onkey(p1.go_up, "Up")
screen.onkey(p1.go_down, "Down")
screen.onkey(p2.go_up, "w")
screen.onkey(p2.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()

    ball.move()

    # Detect ball collision with top or bottom wall
    if ball.ycor() > 285 or ball.ycor() < - 285:
        ball.bounce_y()

    # Detect collision with paddles
    if ball.distance(p1) < 50 and ball.xcor() > 320 or ball.distance(p2) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect when paddle misses the ball and reset the ball in the opposite direction
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.p2_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.p1_point()

screen.exitonclick()
