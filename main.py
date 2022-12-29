from turtle import Screen, Turtle
from ship import Ship
from alien import Alien
from barrier import Barrier


def main():
    screen = Screen()
    screen.bgcolor("black")
    screen.setup(850, 800)
    screen.title("Space Invaders")

    # Declare global variables to access across from other functions.
    global alien_shape, ship_shape, barrier_shape, ship, aliens, ship_bullets, alien_bullets, barriers

    # Add custom shapes for aliens, ship and barriers.
    alien_shape = "alien.gif"
    screen.addshape(alien_shape)

    ship_shape = "ship.gif"
    screen.addshape(ship_shape)

    barrier_shape = "barrier.gif"
    screen.addshape(barrier_shape)

    # Increase the speed and add aliens to the screen.
    screen.tracer(2)

    ship = Ship(ship_shape, position=(0, -350))

    # List of aliens and barriers inside the game.
    aliens = []
    barriers = []

    generate_aliens()
    generate_barriers()

    # Decrease the speed back to normal.
    screen.tracer(1)

    # List of bullets inside the game.
    ship_bullets = []
    alien_bullets = []

    screen.listen()
    screen.onkey(ship.go_left, "a")
    screen.onkey(ship.go_right, "d")
    screen.onkey(ship.go_left, "Left")
    screen.onkey(ship.go_right, "Right")
    screen.onkey(shoot_alien, "space")

    on = True
    lives = 3
    score = 0

    # Create turtles to update score and lives in the screen.
    global score_turtle, lives_turtle
    score_turtle = Turtle()
    lives_turtle = Turtle()

    while on:
        # Add score and lives on the top of the screen and update it when it change.
        update_score(score)
        update_lives(lives)

        # If there are aliens in the list.
        if len(aliens) > 0:
            for alien in aliens:
                # If there are bullets in the list.
                if len(ship_bullets) > 0:
                    for bullet in ship_bullets:
                        if alien.distance(bullet) <= 30:
                            alien.hide()
                            aliens.remove(alien)
                            bullet.hide()
                            ship_bullets.remove(bullet)
                            score += 10
                            score_turtle.reset()
                        if not bullet.hidden:
                            if bullet.ycor() < 410:
                                bullet.move_up()
                            else:
                                ship_bullets.remove(bullet)

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

                # screen.ontimer()

                if lives == 0:
                    return

    screen.exitonclick()


# This will add a bullet to bullets list.
def shoot_alien():
    # Get a new bullet from ship object.
    new_bullet = ship.get_new_bullet()
    if len(ship_bullets) == 0:
        ship_bullets.append(new_bullet)


def shoot_the_ship():
    pass


def generate_aliens():
    # Generate aliens for the first time.
    x = -230
    y = 300
    # Create 3 rows of aliens with 10 in one line.
    for _ in range(3):
        for _ in range(10):
            new_position = (x, y)
            alien = Alien(alien_shape, new_position)
            aliens.append(alien)
            x += 50
        x = -230
        y -= 50


def generate_barriers():
    x = -300
    y = -250
    for _ in range(4):
        new_barrier = Barrier(barrier_shape, position=(x, y))
        barriers.append(new_barrier)
        x += 200


def update_score(score):
    # Life the pen up to not write while moving.
    score_turtle.penup()
    score_turtle.goto([-380, 370])
    # Put the pen down to write.
    score_turtle.pendown()
    # Hide the turtle to now show it while updating the score.
    score_turtle.hideturtle()
    score_turtle.pencolor("red")
    score_turtle.write(f"score: {score}",
                       font=("Silkscreen", 14))


def update_lives(lives):
    lives_turtle.penup()
    lives_turtle.goto([300, 370])
    lives_turtle.pendown()
    lives_turtle.hideturtle()
    lives_turtle.pencolor("red")
    lives_turtle.write(f"Lives ✕ {lives}",
                       font=("Silkscreen", 14))
    lives_turtle.penup()


if __name__ == "__main__":
    main()
