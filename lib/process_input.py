# Example: processing input.


# The main module method.
def main():
    number = eval(input("Enter a number, any number: "))

    print("The square of", number, "is", square(number))


# Square the value of a number.
def square(number):
    return number * number

