from turtle import Turtle
UP = 20

class Paddle(Turtle):
    def __init__(self,positions):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(positions)


    def up(self):
        if self.ycor() > 230:
            pass
        else:
            self.goto(x= self.xcor(), y=self.ycor() + UP)

    def down(self):
        if self.ycor() < -230:
            pass
        else:
            self.goto(x= self.xcor() , y=self.ycor() - UP)

