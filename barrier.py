from turtle import Turtle

class Barrier(Turtle):

    def __init__(self, shape , position):
        super(Barrier, self).__init__(shape=shape)
        self.health = 100
        self.penup()
        self.goto(position)

    def hide(self):
        self.hideturtle()