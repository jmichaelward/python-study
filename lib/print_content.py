# Example: printing content.
# This file is merely a collection of print statements, demonstrating usage of single quotes, double quotes,
# variable printing, and the 'end' parameter that allows a programmer to modify the end of the printed string.
# By default, print passes in "\n" to indicate a line break.


def main():
    print("I am printing content in Python")
    print('I can use single or double quotes for strings, just like other languages')

    name = "Jeremy Ward"

    print("My name is", name, ", which was assigned to a variable.")
    print("The print command adds a space between parameterized values, so there's a space after my name.")
    print("There are probably several ways to remove the space. Two print lines might be one. Let's try it.")
    print("My name is", name, end="")
    print(", which was assigned to a variable.")
    print("In that approach, I modified the 'end' parameter in the print method to remove the carriage return.")
    print("I can change the name variable just like any other language.")

    name = "Jeremy Michael Ward"

    print("I can change the variable to add my middle name:", name)


"""
Adding this conditional guarantees that the module will run automatically if invoked directlry,
but it will not run automatically if imported.
"""
if __name__ == '__main__':
    main()
