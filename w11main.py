import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
t1.fd(200)
t1.penup()
t1.home()
t1.pendown()

def keyup():
    t1.forward(50)

def keydown():
    t1.backward(50)

def keyleft():
    t1.left(90)

def keyright():
    t1.right(90)
def mousegoto(x,y):
    t1.setpos(x,y)
    t1.pos=(x,y)
    if 0<x<200 and y==0:
        print "correct"

    

def addkeys():
    wn.onkey(keyup,"Up")
    wn.onkey(keydown,"Down")
    wn.onkey(keyleft,"Left")
    wn.onkey(keyright,"Right")


wn.onclick(mousegoto)
addkeys()
wn.listen()
turtle.mainloop()

(x,y)=t1.pos()
