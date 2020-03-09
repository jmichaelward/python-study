# Chapter 5: Dictionaries and Structuring Data.
import pprint

birthdays = {
    'Carol': 'Mar 4',
    'Alice': 'Apr 1',
    'Bob': 'Dec 12',
}


def bdays():
    while True:
        print('Enter a name: (blank to quit)')
        name = input()
        if name == '':
            break

        if name in birthdays:
            print(birthdays[name], 'is the birthday of', name)
        else:
            print('I do not have birthday information for', name)
            print('What is their birthday?')
            birthday = input()
            birthdays[name] = birthday
            print('Birthday database updated.')


# values() is dictionary method that can get all of the values from the key-value pairs.
def list_bdays():
    for day in birthdays.values():
        print(day)


# keys() is a method on a dictionary that can get all of the keys from the key-value pairs.
def list_names():
    for name in birthdays.keys():
        print(name)


# items() is a method on a dictionary that get each of the items as a tuple.
def list_items():
    for item in birthdays.items():
        print(item)

    # One can also use multiple assignment to get both the keys and values in separate variables.
    for name, birthday in birthdays.items():
        print(name, ' celebrates a birthday on ', birthday, '.', sep='')


# The get method accepts a default for cases where a key does not exist on a dictionary.
def bring():
    picnic_items = {'apples': 5, 'cups': 2}

    # Prints "I am bringing 2 cups."
    print('I am bringing', str(picnic_items.get('cups', 0)), 'cups.')

    # Prints "I am bringing 2 eggs."
    print('I am bringing', str(picnic_items.get('eggs', 0)), 'eggs.')


# pprint is a module that can let you pretty print dictionaries. It sorts the
def print_bdays():
    pprint.pprint(birthdays)


def main():
    bdays()


if __name__ == '__main__':
    main()
