from turtle import Turtle
move_dist = 20


class Paddle(Turtle):

    def __init__(self, x_pos):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.color('white')
        self.pu()
        self.goto(x_pos, 0)

    def move_up(self):
        self.goto(self.xcor(), self.ycor() + move_dist)

    def move_down(self):
        self.goto(self.xcor(), self.ycor() - move_dist)