from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.y_move = 10
        self.x_move = 10
        self.move_speed = .1
        self.pu()
        self.shape('circle')
        self.color('white')

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)

    def bounce(self):
        self.y_move *= -1

    def collide(self):
        self.x_move *= -1
        self.move_speed *= .9
