from turtle import Turtle


class Bullet(Turtle):

    def __init__(self, position):
        super(Bullet, self).__init__(shape="square")
        self.name = "bullet"
        self.got_hit = False
        self.hideturtle()
        self.color("blue")
        self.shapesize(1, 0.25)
        self.penup()
        self.goto(position)

    def move(self):
        self.showturtle()
        new_y = self.ycor() + 5
        self.goto(self.xcor(), new_y)

    def hide(self):
        self.got_hit = True
        self.hideturtle()
