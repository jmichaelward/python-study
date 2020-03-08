# Import the print_content module from the lib directory.
from lib import print_content
from lib import process_input
from lib.Ball import Ball

# Note: This is made possible by the __init__.py file in the lib directory, which Python uses to identify
# a directory as a collection of modules. Using this approach, I should be able to split up my code into
# separate bits of related functionality, much like I would already do with class-based hierarchies in PHP.


def run_all():
    return 'Y' == input("Run all modules in a row? [Y/n]: ")


# Arbitrary method to create and name a Ball object, then bounce it.
def bounce_ball():
    name = input("Enter a name for a ball you would like to bounce: ")
    size = input("Enter a numeric value for the diameter of the ball, in inches: ")
    ball = Ball(name, size)
    ball.bounce()


def main():
    if run_all():
        print_content.main()
        process_input.main()
        bounce_ball()
        return

    print("Not yet ready to run a selected program.")


main()
