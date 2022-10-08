from turtle import Turtle

UP = 90
DOWN = 270
MOVE = 20


class Player(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.create(x, y)

    def create(self, x, y):
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.shape("square")
        self.goto(x, y)

    def up(self):
        new_y = self.ycor() + 20
        new_x = self.xcor()
        if new_y < 280:
            self.goto(new_x, new_y)

    def down(self):
        new_y = self.ycor() - 20
        new_x = self.xcor()
        if new_y > -260:
            self.goto(new_x, new_y)
