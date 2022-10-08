import time
from turtle import Screen, Turtle
from player import Player
from ball import Ball

# Screen Setup and codes
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)
screen.listen()

# Create player lines on left and right
r_player = Player(370, 0)
l_player = Player(-380, 0)

# Ball Create
ball = Ball()

# control Player Board
screen.onkey(r_player.up, "Up")
screen.onkey(r_player.down, "Down")
screen.onkey(l_player.up, "w")
screen.onkey(l_player.down, "s")


# Game over function code
def game_over():
    turtle = Turtle()
    turtle.pu()
    turtle.hideturtle()
    turtle.color("white")
    turtle.write("GAME OVER !!!", align='center', font=('Arial', 74, 'normal'))


# Middle Line function
def middle_line(x):
    turtle = Turtle()
    turtle.pu()
    turtle.goto(0, 300)
    turtle.seth(270)
    # turtle.hideturtle()
    turtle.color("white")
    turtle.shape("square")
    turtle.fd(x)


for x in range(30):
    if x % 2 == 0:
        y = 20 * x
        middle_line(y)

is_game_on = True
while is_game_on:
    ball.move_right()
    time.sleep(0.1)
    screen.update()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    if ball.distance(l_player) < 50 and ball.xcor() < -350 or ball.distance(r_player) < 50 and ball.xcor() > 340:
        ball.x_bounce()

    if ball.xcor() < -370:
        ball.reset_position()

    if ball.xcor() > 380:
        ball.reset_position()

screen.exitonclick()
