# Prints a 2x4 and a 4x4 grid
#
# Author: Ernest McDowell
# Date: 31JAN2022
#
# Excersise originating from Think Python 2nd Edition by Allen B. Downy
#

def do_twice(f):
    f()
    f()

def do_four(f):
    do_twice(f)
    do_twice(f)

def print_beam():
    print('+ - - - - - ', end=' ')

def print_post():
    print('|           ', end=' ')

def print_beams():
    do_twice(print_beam)
    print('+')

def print_posts():
    do_twice(print_post)
    print('|')

def print_rows():
    print_beams()
    do_four(print_posts)

def print_grid():
    do_twice(print_rows)
    print_beams()


print_grid()
