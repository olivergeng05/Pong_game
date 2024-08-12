from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.pu()
        self.hideturtle()
        self.right_score = 0
        self.left_score = 0
        self.goto(-100, 200)
        self.write(self.left_score, align='center', font=('Courier', 80, 'normal'))
        self.goto(100,200)
        self.write(self.right_score, align='center', font=('Courier', 80, 'normal'))

    def right_up(self):
        self.clear()
        self.right_score += 1
        self.goto(-100, 200)
        self.write(self.left_score, align='center', font=('Courier', 80, 'normal'))
        self.goto(100, 200)
        self.write(self.right_score, align='center', font=('Courier', 80, 'normal'))
    def left_up(self):
        self.clear()
        self.left_score += 1
        self.goto(-100, 200)
        self.write(self.left_score, align='center', font=('Courier', 80, 'normal'))
        self.goto(100, 200)
        self.write(self.right_score, align='center', font=('Courier', 80, 'normal'))
