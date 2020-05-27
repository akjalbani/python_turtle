# Demo for using list, nested loops and functions
# @ Author : Akhtar Jalbani
# Tested on : python online IDE REPL.IT

import turtle
def Square_with_color(length,color):
  turtle.color(color)
  turtle.begin_fill()
  for i in range(4):
    turtle.forward(length)
    turtle.left(90)
  turtle.forward(length)
  turtle.end_fill()

colors = ['red','black','red','black']
rows = [1,2,3]
pos = 0
for row in rows:
  for color in colors:
    Square_with_color(100,color)
  turtle.penup()
  pos = pos + 100
  turtle.goto(0,pos)
  turtle.pendown()
  colors.reverse()

