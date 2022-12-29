from turtle import Turtle
from bullet import Bullet


class Ship(Turtle):

    def __init__(self, shape, position):
        super(Ship, self).__init__(shape=shape)
        self.position = position
        self.penup()
        self.goto(position)

    # Go back to started position.
    def reset(self):
        self.hideturtle()
        self.goto(self.position)
        self.showturtle()

    def go_left(self):
        new_x = self.xcor() - 40
        # If ship is not close to left edge.
        if new_x >= -400:
            self.goto(new_x, self.ycor())

    def go_right(self):
        new_x = self.xcor() + 40
        # If ship is not close to right edge.
        if new_x <= 400:
            self.goto(new_x, self.ycor())

    # Get a new bullet from the ship's position.
    def get_new_bullet(self):
        new_bullet = Bullet(
            shape="square", color="blue" , position=(self.xcor(), self.ycor()))
        return new_bullet
