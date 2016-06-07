import turtle
import math
import time
wn=turtle.Screen()
d1=turtle.Turtle()
wn.bgcolor("Lightpink")
size=100
d1.speed(100)

def Circle(pos,size):
 d1.penup()
 d1.goto(pos)
 d1.pendown()
 d1.circle(size)




def s(pos,size):
 d1.penup()
 d1.goto(pos)
 d1.pendown()
 for i in range(0,4):
  d1.fd(100)
  d1.right(90)

pos=(200,200)
size=100
Circle(pos,size)

pos=(-200,200)
size=50
Circle(pos,size)

pos=(0,-250)
size=80
Circle(pos,size)

pos=(-250,-150)
size=50
s(pos,size)

pos=(300,-150)
size=100
s(pos,size)

pos=(0,250)
size=80
s(pos,size)

score=0



def isincircle(center,radius,curpos):
    if math.sqrt(math.pow(center[0]-curpos[0],2)+ math.pow(center[1]-curpos[1],2))<=radius:
        score=score+10
        print "your score is", score

def isinsquare(coord,curpos):
    if coord[0][0]<=curpos[0]<=coord[1][0] and coord[0][1]<=curpos[1]<=coord[1][1]:
        score=score+5
        print "your score is", score

def end():
    if score>=100:
        wn.bye()
def record(): 
    played=open('record.txt','a') 
    msg=time.strftime('%Y.%m.%d-%H:%M:%S') 
    played.write('\n'+msg+'\t'+"Player Score is"+'\t'+score) 
    played.close() 









t2=turtle.Turtle()
t2.shape("turtle")
t2.penup()

def k1():
    t2.forward(45)
    curpos=t2.pos()
    isincircle((-200,250),50,curpos)
    isincircle((0,-170),80,curpos)
    isincircle((200,300),100,curpos)
    coord=[(-250,-150),(-200,-200)]
    isinsquare(coord,curpos)
    coord=[(0,250),(80,170)]
    isinsquare(coord,curpos)
    coord=[(300,-150),(400,-250)]
    isinsquare(coord,curpos)
    end()

def k2():
    t2.left(45)
    curpos=t2.pos()
    isincircle((-200,250),50,curpos)
    isincircle((0,-170),80,curpos)
    isincircle((200,300),100,curpos)
    coord=[(-250,-150),(-200,-200)]
    isinsquare(coord,curpos)
    coord=[(0,250),(80,170)]
    isinsquare(coord,curpos)
    coord=[(300,-150),(400,-250)]
    isinsquare(coord,curpos)
    end()

def k3():
    t2.right(45)

def k4():
    t2.back(45)


wn.onkey(k1, "Up")
wn.onkey(k2, "Left")
wn.onkey(k3, "Right")
wn.onkey(k4, "Down")

wn.listen()
turtle.mainloop()