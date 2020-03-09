#! python3
# pw.py - An insecure password locker program.
"""
This is a modified version of the program in Chapter 6 of Al Sweigart's book. Instead of copying the password to the
clipboard, I'm simply printing it to the console. I've also modified the program to check for a couple of subcommands:
list or get. `list` will list the available accounts in the command line, which of course could get quite long if there
were hundreds of accounts. `get` will get the password from the dictionary, if available, and print it to the console.

Additionally, I have moved the main logic for the application into the main method, and am using the tripe-quote
to print out a full list of commands if the user (me!) did not provide any arguments to the command.
"""
import sys

PASSWORDS = {
    'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
    'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
    'luggage': '12345',
}


def get_password():
    if len(sys.argv) != 3:
        show_help()
        return

    account = sys.argv[2]
    print(PASSWORDS.get(account, account + ' not found.'))


def show_help():
    print('''
        Usage: python pw.py [command] - copy account password
        
        Available commands:
        - list: List available accounts.
        - get [account]: Get the password for a given account.
        ''')


def list_accounts():
    for account in PASSWORDS.keys():
        print(account)


def main():
    if len(sys.argv) < 2:
        show_help()
        sys.exit()

    command = commands.get(sys.argv[1], show_help)
    command()


commands = {
    'list': list_accounts,
    'get': get_password,
}


if __name__ == '__main__':
    main()
