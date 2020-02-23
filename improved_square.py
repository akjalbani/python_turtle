###################################################
# THis is a simple python program to run turtle graphics
# Author : Akhtar Jalbani
# Version: 0.2
# This is improved version using loop
#################################################
import turtle
from typing import List

wn = turtle.Screen()
wn.bgcolor("light green")
wn.title("Turtle")
myturtle = turtle.Turtle()

for side in range(4):
    myturtle.forward(100)
    myturtle.left(90)
turtle.done()
