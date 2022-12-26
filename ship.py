from turtle import Turtle
from bullet import Bullet


class Ship(Turtle):

    def __init__(self, position):
        super(Ship, self).__init__(shape="classic")
        self.color("blue")
        self.shapesize(stretch_wid=3, stretch_len=3)
        self.penup()
        self.tilt(90)
        self.goto(position)

    def go_left(self):
        new_x = self.xcor() - 40
        if new_x >= -400:
            self.goto(new_x, self.ycor())

    def go_right(self):
        new_x = self.xcor() + 40
        if new_x <= 400:
            self.goto(new_x, self.ycor())

    def get_new_bullet(self):
        new_bullet = Bullet(
            shape="square", position=(self.xcor(), self.ycor()))
        return new_bullet
