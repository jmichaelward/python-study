# Import the print_content module from the lib directory.
from lib import print_content
from lib import process_input

# Note: This is made possible by the __init__.py file in the lib directory, which Python uses to identify
# a directory as a collection of modules. Using this approach, I should be able to split up my code into
# separate bits of related functionality, much like I would already do with class-based hierarchies in PHP.


def main():
    print_content.main()
    process_input.main()


main()
