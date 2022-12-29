from turtle import Turtle

class Barrier(Turtle):

    def __init__(self, shape , position):
        super(Barrier, self).__init__(shape=shape)
        self.penup()
        self.goto(position)