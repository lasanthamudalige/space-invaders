from turtle import Screen
from bullet import Bullet
from ship import Ship
from alien import Alien
import random


def main():
    screen = Screen()
    screen.bgcolor("black")
    screen.setup(850, 800)
    screen.title("Space Invaders")

    global ship
    ship = Ship(position=(0, -350))

    global objects
    objects = []

    get_new_alien()

    screen.listen()
    screen.onkey(ship.go_left, "a")
    screen.onkey(ship.go_right, "d")
    screen.onkey(ship.go_left, "Left")
    screen.onkey(ship.go_right, "Right")
    screen.onkey(shoot, "space")

    on = True
    while on:
        for object in objects:
            if object.name == "alien":
                object.move()
            if object.name == "bullet":
                if object.ycor() < 410:
                    object.move()
                else:
                    objects.remove(object)

    screen.exitonclick()


def shoot():
    bullet = Bullet(position=(ship.xcor(), ship.ycor()))
    objects.append(bullet)


def get_new_alien():
    random_y = random.randint(-400, 400)
    new_position = (random_y, 350)
    alien = Alien(new_position)
    objects.append(alien)


if __name__ == "__main__":
    main()
