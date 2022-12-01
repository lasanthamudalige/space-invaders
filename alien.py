from turtle import Turtle


class Alien(Turtle):

    def __init__(self, position):
        super(Alien, self).__init__(shape="square")
        self.direction = "left"
        self.hideturtle()
        self.color("blue")
        self.shapesize(1, 1)
        self.penup()
        self.goto(position)

    def move_left(self):
        self.showturtle()
        new_x = self.xcor() - 10
        if new_x >= -410:
            self.goto(new_x, self.ycor())

    def move_right(self):
        self.showturtle()
        new_x = self.xcor() + 10
        if new_x <= 410:
            self.goto(new_x, self.ycor())
