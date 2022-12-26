from turtle import Screen, Turtle
from ship import Ship
from alien import Alien


def main():
    screen = Screen()
    screen.bgcolor("black")
    screen.setup(850, 800)
    screen.title("Space Invaders")
    # Increase the speed and add aliens to the screen.
    screen.tracer(2)

    global ship
    ship = Ship(position=(0, -350))

    # List of aliens inside the game.
    global aliens
    aliens = []

    generate_aliens()

    # Decrease the speed back to normal.
    screen.tracer(2)

    # List of bullets inside the game.
    global bullets
    bullets = []

    screen.listen()
    screen.onkey(ship.go_left, "a")
    screen.onkey(ship.go_right, "d")
    screen.onkey(ship.go_left, "Left")
    screen.onkey(ship.go_right, "Right")
    screen.onkey(shoot, "space")

    on = True
    lives = 3
    score = 0

    # Create turtles to update score and lives in the screen.
    global score_turtle, lives_turtle
    score_turtle = Turtle()
    lives_turtle = Turtle()

    while on:
        # If there are aliens in the list.
        if len(aliens) > 0:
            for alien in aliens:
                # If there are bullets in the list.
                if len(bullets) > 0:
                    for bullet in bullets:
                        if alien.distance(bullet) <= 30:
                            alien.hide()
                            aliens.remove(alien)
                            bullet.hide()
                            bullets.remove(bullet)
                            score += 10
                            score_turtle.reset()
                        if not bullet.hidden:
                            if bullet.ycor() < 410:
                                bullet.move_up()
                            else:
                                bullets.remove(bullet)

                if alien.direction == "left":
                    if alien.xcor() > -380:
                        alien.move_left()
                    else:
                        for alien in reversed(aliens):
                            alien.direction = "right"
                            if alien.ycor() > -300:
                                alien.move_down()

                if alien.direction == "right":
                    if alien.xcor() < 380:
                        alien.move_right()
                    else:
                        for alien in reversed(aliens):
                            alien.direction = "left"
                            if alien.ycor() > -300:
                                alien.move_down()

                if lives == 0:
                    return

            update_score(score)
            update_lives(lives)

    screen.exitonclick()


def shoot():
    # Get a new bullet from ship object.
    new_bullet = ship.get_new_bullet()
    if len(bullets) == 0:
        bullets.append(new_bullet)


def generate_aliens():
    # Generate aliens for the first time.
    x = -230
    y = 350
    # Create 3 rows of aliens with 10 in one line.
    for _ in range(3):
        for _ in range(10):
            new_position = (x, y)
            alien = Alien(new_position)
            aliens.append(alien)
            x += 50
        x = -230
        y -= 50


def update_score(score):
    score_turtle.penup()
    score_turtle.goto([-380, 370])
    score_turtle.pendown()
    score_turtle.hideturtle()
    score_turtle.pencolor("red")
    score_turtle.write(f"score: {score}",
                       font=("Arial", 12, "normal"))


def update_lives(lives):
    lives_turtle.penup()
    lives_turtle.goto([320, 370])
    lives_turtle.pendown()
    lives_turtle.hideturtle()
    lives_turtle.pencolor("red")
    lives_turtle.write(f"Lives ✕ {lives}",
                       font=("Verdana", 12, "normal"))
    lives_turtle.penup()


if __name__ == "__main__":
    main()
