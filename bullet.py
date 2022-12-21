from turtle import Turtle


class Bullet(Turtle):

    def __init__(self, position):
        super(Bullet, self).__init__(shape="circle")
        self.hideturtle()
        self.color("blue")
        self.shapesize(0.5, 0.5)
        self.name = "bullet"
        self.penup()
        self.goto(position)

    def move(self):
        self.showturtle()
        new_y = self.ycor() + 5
        self.goto(self.xcor(), new_y)
