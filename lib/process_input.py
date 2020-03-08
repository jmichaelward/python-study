# Example: processing input.


# The main module method.
def main():
    number = eval(input("Enter a number, any number: "))

    print("The square of", number, "is", square(number))


# Square the value of a number.
def square(number):
    return number * number


"""
Adding this conditional guarantees that the module will run automatically if invoked directly,
but it will not run automatically if imported.
"""
if __name__ == '__main__':
    main()
