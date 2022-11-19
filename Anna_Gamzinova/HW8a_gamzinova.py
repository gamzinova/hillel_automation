# print function using stdout
import sys


def print_function(*argv):
    """
    The print function prints to the standard output device using stdout
    """
    sys.stdout.write(''.join(map(str, argv)))
    sys.stdout.write('\n')


# tests:
number = 5
print_function(f'Anna Yossi {number}')
print_function('Anna\n''Elia')
print_function('Anna' + 'Elia')
print_function({'red', 'green', 'blue'})
