from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.create()
        self.x_move = 10
        self.y_move = 10

    def create(self):
        self.pu()
        self.shape("circle")
        self.color("white")
        self.goto(0, 0)

    def move_right(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def move_left(self):
        new_x = self.xcor() - self.x_move
        new_y = self.ycor() - self.y_move
        self.goto(new_x, new_y)

    def y_bounce(self):
        self.y_move *= -1

    def x_bounce(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.x_bounce()

