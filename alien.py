from turtle import Turtle


class Alien(Turtle):

    def __init__(self, position):
        super(Alien, self).__init__(shape="square")
        self.name = "alien"
        self.got_hit = False
        self.hideturtle()
        self.color("white")
        self.shapesize(1, 1)
        self.penup()
        self.goto(position)

    def move(self):
        self.showturtle()
        new_y = self.ycor() - 5
        if new_y <= 410:
            self.goto(self.xcor(), new_y)

    def hide(self):
        self.got_hit = True
        self.hideturtle()
