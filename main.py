import turtle

my_turtle = turtle.Turtle()

def square():
  my_turtle.right(90)
  my_turtle.forward(50)
  my_turtle.right(90)
  my_turtle.forward(50)
  my_turtle.right(90)
  my_turtle.forward(50)
  my_turtle.right(160)
  my_turtle.forward(50)
  
for i in range(80):
  square()
  