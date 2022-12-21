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

    global aliens
    aliens = []

    for _ in range(10):
        get_new_alien()

    global bullets
    bullets = []

    screen.listen()
    screen.onkey(ship.go_left, "a")
    screen.onkey(ship.go_right, "d")
    screen.onkey(ship.go_left, "Left")
    screen.onkey(ship.go_right, "Right")
    screen.onkey(shoot, "space")

    on = True
    while on:
        for alien in aliens:
            for bullet in bullets:
                if alien.distance(bullet) <= 25:
                    aliens.remove(alien)
            if alien.ycor() < 410:
                alien.move()

        for bullet in bullets:
            if bullet.ycor() < 410:
                bullet.move()
            else:
                bullets.remove(bullet)

    screen.exitonclick()


def shoot():
    bullet = Bullet(position=(ship.xcor(), ship.ycor()))
    bullets.append(bullet)


def get_new_alien():
    random_y = random.randint(-400, 400)
    new_position = (random_y, 350)
    alien = Alien(new_position)
    aliens.append(alien)


if __name__ == "__main__":
    main()
