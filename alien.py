from turtle import Turtle
from bullet import Bullet


class Alien(Turtle):

    def __init__(self, position):
        super(Alien, self).__init__(shape="square")
        self.name = "alien"
        self.direction = "left"
        self.got_hit = False
        self.hideturtle()
        self.color("white")
        self.shapesize(1, 1)
        self.penup()
        self.goto(position)

    def move_down(self):
        self.showturtle()
        new_y = self.ycor() - 40
        if new_y <= 410:
            self.goto(self.xcor(), new_y)

    def move_left(self):
        new_x = self.xcor() - 40
        if new_x >= -400:
            self.goto(new_x, self.ycor())

    def move_right(self):
        new_x = self.xcor() + 40
        if new_x <= 400:
            self.goto(new_x, self.ycor())

    def hide(self):
        self.got_hit = True
        self.hideturtle()

    def get_new_bullet(self):
        new_bullet = Bullet(
            shape="circle", position=(self.xcor(), self.ycor()))
        return new_bullet
