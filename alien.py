from turtle import Turtle
from bullet import Bullet


class Alien(Turtle):

    def __init__(self, position):
        super(Alien, self).__init__(shape="square")
        self.name = "alien"
        self.direction = "left"
        self.hideturtle()
        self.color("white")
        self.shapesize(1, 1)
        self.penup()
        self.goto(position)
        self.showturtle()

    def move_down(self):
        new_y = self.ycor() - 40
        self.goto(self.xcor(), new_y)

    def move_left(self):
        new_x = self.xcor() - 40
        self.goto(new_x, self.ycor())

    def move_right(self):
        new_x = self.xcor() + 40
        self.goto(new_x, self.ycor())

    def hide(self):
        self.hideturtle()

    def get_new_bullet(self):
        new_bullet = Bullet(
            shape="circle", position=(self.xcor(), self.ycor()))
        return new_bullet
