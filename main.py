from turtle import Screen
from bullet import Bullet
from ship import Ship
from alien import Alien


def main():
    screen = Screen()
    screen.bgcolor("black")
    screen.setup(850, 800)
    screen.title("Space Invaders")
    screen.tracer(1)

    global ship
    ship = Ship(position=(0, -350))

    aliens = []
    x_coordinates = [-200, -150, -100, -50, 0, 50, 100, 150, 200]
    for x in x_coordinates:
        location = (x, 350)
        alien = Alien(position=location)
        aliens.append(alien)

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
            # Move alien from left to right
            if alien.direction == "left":
                if alien.xcor() == -410:
                    alien.direction = "right"
                else:
                    alien.move_left()
            elif alien.direction == "right":
                if alien.xcor() == 410:
                    alien.direction = "down"
                else:
                    alien.move_right()
            # Move alien 1 row down when alien reach right
            elif alien.direction == "down":
                new_y = alien.ycor() - 10
                alien.goto(x=alien.xcor(), y=new_y)
                alien.direction = "left"

        for bullet in bullets:
            if bullet.ycor() < 410:
                bullet.move()
            else:
                bullets.remove(bullet)

    screen.exitonclick()


def shoot():
    bullet = Bullet(position=(ship.xcor(), ship.ycor()))
    bullets.append(bullet)


if __name__ == "__main__":
    main()
