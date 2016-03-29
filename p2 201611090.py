import turtle
wn=turtle.Screen()
t1=turtle.Turtle()

def makeSquare(size,bigger,sides,angle):
     for i in range(0,sides):
          if(i%2):
              size=size+bigger
          t1.fd(size)
          t1.right(90)

makelSquare(20,20,30,90)

wn.exitonclick()