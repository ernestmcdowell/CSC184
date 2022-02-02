#
#
#
#
# Use a function to draw a square using for loop and turtle

import turtle
import math


bob = turtle.Turtle()

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

def polygon(t, n, length=5):
    for i in range(n):
        angles = 360 / n
        t.fd(length)
        t.lt(angles)

def draw_circle(t, r, n):
    circumference = 2 * math.pi * r
    length = circumference / n
    polygon(t, n, length=5)

def draw_arc(t, r, angle):
    arch_length = 2 * math.pi * r * angle / 360
    n = int(arch_length / 3) + 1
    step_length = arch_length / n
    step_angle = angle / n
    
    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)
        r+2

draw_arc(bob, r=35, angle=360)
draw_arc(bob, r=40, angle=360)
draw_arc(bob, r=45, angle=360)
draw_arc(bob, r=50, angle=360)
draw_arc(bob, r=55, angle=360)
draw_arc(bob, r=60, angle=360)
draw_arc(bob, r=65, angle=360)
draw_arc(bob, r=65, angle=360)
draw_arc(bob, r=70, angle=360)

turtle.mainloop()
    
