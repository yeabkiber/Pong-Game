import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard

screen = Screen()
screen.title('Pong')
screen.setup(width=800,height=600)
screen.bgcolor('black')
screen.tracer(0)

l_paddle = Paddle((-360,0))
r_paddle = Paddle((360,0))

ball = Ball()



scoreboard = ScoreBoard()



screen.listen()
screen.onkey(key='Up',fun=r_paddle.up)
screen.onkey(key='Down',fun=r_paddle.down)
screen.onkey(key='w',fun=l_paddle.up)
screen.onkey(key='s',fun=l_paddle.down)


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # needs to bounce
        ball.bounce_y()

    # Detect Collision with the r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()


    # Detect R Paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
        if scoreboard.total_score >= 5:
            game_is_on = False


    # Detect L Paddle misses

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
        if scoreboard.total_score >= 5:
            game_is_on = False








screen.exitonclick()