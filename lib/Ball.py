"""
A generic object to represent a physical ball.

The purpose of this object is to learn the basics of how classes are structured
in Python.
"""


class Ball:
    # Class constructor.
    def __init__(self, name, diameter):
        self.name = name
        self.diameter = diameter

    """
    In actuality, we most likely wouldn't have a private getter, but I want to see whether
    my application fails by trying to access a method that uses double-underscores, since it's
    supposed to indicate private object access.
    """
    def __get_name(self):
        return self.name

    # Get the diameter of the ball.
    def get_diameter(self):
        return self.diameter

    # Bounce the ball.
    def bounce(self):
        print("Bouncing the ball named", self.name)


