import turtle
wn = turtle.Screen()
turtle1= turtle.Turtle()
length = 100
angle1 = 90
angle2 = 120
sides = 5
print("--MENU--")
print("1. draw a square")
print("2. draw a triangle")
print("3. draw a hexagon")
print("4. draw a circle")
print("5. Exit")
print("-------------------")
option = int(input("Type your Option(1--5)-> "))
if option == 1:
  turtle1.forward(length)
  turtle1.left(angle1)
  turtle1.forward(length)
  turtle1.left(angle1)
  turtle1.forward(length)
  turtle1.left(angle1)
  turtle1.forward(length)
  turtle1.left(angle1)
if option ==2:
  turtle1.forward(length)
  turtle1.left(angle2)
  turtle1.forward(length)
  turtle1.left(angle2)
  turtle1.forward(length)
  turtle1.left(angle2)
if option ==3:
  turtle1.forward(length)
  turtle1.left(360/sides)
  turtle1.forward(length)
  turtle1.left(360/sides)
  turtle1.forward(length)
  turtle1.left(360/sides)
  turtle1.forward(length)
  turtle1.left(360/sides)
  turtle1.forward(length)
  turtle1.left(360/sides)
if option == 4:
  turtle1.circle(100)
if option == 5:
  print("Enjoyed! working with turtle")
    
else:
    print("You have selected wrong option")
    