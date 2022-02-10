# import time


# #nested conditionals example

# x = input("Enter number for x: ")
# y = input("Enter a number for y: ")

# if x == y:
#     print('x and y are equal')
# else:
#     if x < y:
#         print('x is less than y')
#     else:
#         print('x is greater than y')

# # recursion example

# def print_n(s, n):
#     if n <= 0:
#         return
#     print(s)
#     print_n(s, n-1)
# print_n("Duck", 5)

# def countdown(n):
#     if n <= 0:
#         print('Blastoff!')
#     else:
#         print(n)
#         countdown(n-1)
# countdown(5)

"""This module contains a code example related to
Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
Copyright 2015 Allen Downey
License: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

import turtle


def koch(t, n):
    """Draws a koch curve with length n."""
    if n < 10:
        t.fd(n)
        return
    m = n/3
    koch(t, m)
    t.lt(60)
    koch(t, m)
    t.rt(120)
    koch(t, m)
    t.lt(60)
    koch(t, m)


def snowflake(t, n):
    """Draws a snowflake (a triangle with a Koch curve for each side)."""
    for i in range(3):
        koch(t, n)
        t.rt(120)


bob = turtle.Turtle()

bob.pu()
bob.goto(-150, 90)
bob.pd()
snowflake(bob, 300)

turtle.mainloop()