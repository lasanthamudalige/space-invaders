from turtle import Turtle


class Bullet(Turtle):

    def __init__(self, shape, position):
        super(Bullet, self).__init__(shape=shape)
        self.hidden = False
        self.hideturtle()
        self.color("blue")
        self.shapesize(1, 0.25)
        self.penup()
        self.goto(position)

    def move_up(self):
        self.showturtle()
        # Add 5 from the current y position from the bullet.
        new_y = self.ycor() + 5
        self.goto(self.xcor(), new_y)

    def move_down(self):
        self.showturtle()
        # Reduce 5 from the current y position from the bullet.
        new_y = self.ycor() - 5
        self.goto(self.xcor(), new_y)

    # Hide the bullet from the screen
    def hide(self):
        self.hidden = True
        self.hideturtle()
