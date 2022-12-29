from turtle import Turtle
from bullet import Bullet


class Alien(Turtle):

    def __init__(self, shape,  position):
        super(Alien, self).__init__(shape=shape)
        self.direction = "left"
        self.hideturtle()
        self.penup()
        self.goto(position)
        self.showturtle()

    def move_down(self):
        # Reduce 40 from the current y position of the alien.
        new_y = self.ycor() - 40
        self.goto(self.xcor(), new_y)

    def move_left(self):
        # Reduce 40 from the current x position of the alien.
        new_x = self.xcor() - 40
        self.goto(new_x, self.ycor())

    def move_right(self):
        # Add 40 to current x position of the alien.
        new_x = self.xcor() + 40
        self.goto(new_x, self.ycor())

    def hide(self):
        self.hideturtle()

    # Get a new bullet from the alien's position.
    def get_new_bullet(self):
        new_bullet = Bullet(
            shape="circle", position=(self.xcor(), self.ycor()))
        return new_bullet
