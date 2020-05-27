###################################################
# THis is a simple python program to run turtle graphics
# Author : Akhtar Jalbani
# Version: 0.3
# This is improved version using function
# Tested on : python IDLE
#################################################
import turtle

# function defination
def square(length,angle):
    for side in range(4):
        myturtle.forward(length)
        myturtle.left(angle)


wn = turtle.Screen()
wn.bgcolor("light green")
wn.title("Turtle")
myturtle = turtle.Turtle()
myturtle.speed(10)
square(100,90)
turtle.done()

