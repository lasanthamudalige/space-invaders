from turtle import Turtle


class Bullet(Turtle):

    def __init__(self, position):
        super(Bullet, self).__init__(shape="square")
        self.hideturtle()
        self.color("blue")
        self.shapesize(1, 0.25)
        self.name = "bullet"
        self.penup()
        self.goto(position)

    def move(self):
        self.showturtle()
        new_y = self.ycor() + 5
        self.goto(self.xcor(), new_y)
