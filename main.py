from turtle import Screen, Turtle
from ship import Ship
from alien import Alien
from barrier import Barrier
import random
from time import sleep
import sys


def main():
    # Declare global variables to access across from other functions.
    global screen
    screen = Screen()
    screen.bgcolor("black")
    screen.setup(850, 800)
    screen.title("Space Invaders")

    # Add custom shapes for aliens, ship and barriers.
    global alien_shape
    alien_shape = "icons/alien.gif"
    screen.addshape(alien_shape)

    global ship_shape
    ship_shape = "icons/ship.gif"
    screen.addshape(ship_shape)

    global barrier_shape
    barrier_shape = "icons/barrier.gif"
    screen.addshape(barrier_shape)

    # Increase the speed and add aliens to the screen.
    screen.tracer(2)

    global ship
    ship = Ship(ship_shape, position=(0, -350))

    # List of aliens and barriers inside the game.
    global aliens, barriers
    aliens = []
    barriers = []

    generate_aliens()
    generate_barriers()

    # Decrease the speed back to normal.
    screen.tracer(1)

    # List of bullets inside the game.
    global ship_bullets, alien_bullets
    ship_bullets = []
    alien_bullets = []

    # Move the ship left and right by listening to key presses.
    screen.listen()
    screen.onkey(ship.go_left, "a")
    screen.onkey(ship.go_right, "d")
    screen.onkey(ship.go_left, "Left")
    screen.onkey(ship.go_right, "Right")
    screen.onkey(shoot_alien, "space")

    on = True
    lives = 3
    score = 0
    # This will start shooting for.
    start_to_shoot = False

    # Create turtles to update score and lives in the screen.
    global score_turtle, lives_turtle
    score_turtle = Turtle()
    lives_turtle = Turtle()

    # Turtle to show end message and score in the game
    global end_turtle
    end_turtle = Turtle()

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
                        # If bullet distance from the alien is less than 20.
                        if alien.distance(bullet) <= 20:
                            alien.hide()
                            aliens.remove(alien)
                            bullet.hide()
                            ship_bullets.remove(bullet)
                            score += 10
                            score_turtle.reset()
                        elif not bullet.hidden:
                            # If bullet is outside of the screen.
                            if bullet.ycor() < 410:
                                bullet.move_up()
                            else:
                                ship_bullets.remove(bullet)
                        for barrier in barriers:
                            # If bullet distance from the barrier is less than 50 and barrier health is greater than 0.
                            if barrier.distance(bullet) <= 50 and barrier.health > 0:
                                bullet.hide()
                                ship_bullets.remove(bullet)
                                barrier.health -= 20
                            # If barrier health is less than or equal to 0.
                            elif barrier.health <= 0:
                                barriers.remove(barrier)
                                barrier.hide()

                if alien.direction == "left":
                    # If alien direction is left and x coordination is greater than -380.
                    if alien.xcor() > -380:
                        alien.move_left()
                    # else change alien direction property to right.
                    else:
                        for alien in reversed(aliens):
                            alien.direction = "right"
                            # Move down all aliens if the current alien is close to the screen edge and break out of all for loops.
                            if alien.ycor() > -300:
                                alien.move_down()
                        break
                if alien.direction == "right":
                    if alien.xcor() < 380:
                        alien.move_right()
                    else:
                        for alien in reversed(aliens):
                            alien.direction = "left"
                            if alien.ycor() > -300:
                                alien.move_down()
                        break

                # This function will start aliens to shoot downwards for the first time.
                if not start_to_shoot:
                    shoot_the_ship()
                    start_to_shoot = True

                for bullet in alien_bullets:
                    # If bullet is still in the screen.
                    if bullet.ycor() > -410:
                        # If the bullet hit the ship.
                        if bullet.distance(ship) <= 15:
                            bullet.hide()
                            alien_bullets.remove(bullet)
                            lives -= 1
                            ship.reset()
                        else:
                            bullet.move_down()
                    else:
                        alien_bullets.remove(bullet)

                    for barrier in barriers:
                        if barrier.distance(bullet) <= 48 and barrier.health > 0:
                            bullet.hide()
                            alien_bullets.remove(bullet)
                            barrier.health -= 20
                        elif barrier.health <= 0:
                            barriers.remove(barrier)
                            barrier.hide()

                # If all lives are over end the game after showing the score.
                if lives == 0:
                    on = False
                    end_game(score)
                    sleep(5)
                    sys.exit(0)

    screen.exitonclick()


# This will add a bullet to bullets list.
def shoot_alien():
    # Get a new bullet from ship object.
    new_bullet = ship.get_new_bullet()
    if len(ship_bullets) == 0:
        ship_bullets.append(new_bullet)


def shoot_the_ship():
    # Select a random alien to shoot.
    random_alien = random.choice(aliens)
    new_bullet = random_alien.get_new_bullet()
    alien_bullets.append(new_bullet)
    screen.ontimer(shoot_the_ship, 5000)


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
    # Create 4 barriers on the screen.
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
    # Clear the previous drawing before writing.
    score_turtle.clear()
    score_turtle.write(f"score: {score}",
                       font=("Silkscreen", 14))


def update_lives(lives):
    lives_turtle.penup()
    lives_turtle.goto([300, 370])
    lives_turtle.pendown()
    lives_turtle.hideturtle()
    lives_turtle.pencolor("red")
    lives_turtle.clear()
    lives_turtle.write(f"Lives ✕ {lives}",
                       font=("Silkscreen", 14))
    lives_turtle.penup()


# This to show end message and score.
def end_game(score):
    screen.clear()
    screen.bgcolor("black")
    end_turtle.hideturtle()
    end_turtle.penup()
    end_turtle.goto((-130, 200))
    end_turtle.pendown()
    end_turtle.pencolor("red")
    end_turtle.write("Game Over!", font=("Silkscreen", 30))
    end_turtle.penup()
    end_turtle.goto((-140, 100))
    end_turtle.pendown()
    end_turtle.write(
        f"Your score: {score}", font=("Silkscreen", 25))


if __name__ == "__main__":
    main()
