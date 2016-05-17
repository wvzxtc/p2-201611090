import turtle 
wn=turtle.Screen() 
t1=turtle.Turtle() 
import math

def drawCircle(center,radius,pos): 
    return 0<math.sqrt(math.pow(center[0]-pos[0],2) + math.pow(center[1]-pos[1],2))<radius 
 
def circle((x,y),size): 
    t1.setpos(x,y) 
    t1.setheading(0) 
    t1.fillcolor("BLUE") 
    t1.begin_fill()
    t1.circle(size) 
    t1.end_fill() 
def rectangle(curpos,coord): 
    xs=coord[0][0] 
    xe=coord[1][0] 
    ys=coord[0][1] 
    ye=coord[1][1] 
    return xs<=curpos[0]<=xe and ys<=curpos[1]<=ye 
def 1((x,y),size): 
    angle = 90 
    t1.fillcolor("RED")
    t1.begin_fill()
    t1.setpos(x,y)
    t1.setheading(0)
    for i in range(4): 
        t1.forward(size) 
        t1.right(angle)
    t1.end_fill()
 
def 2((x,y),size):
    angle = 90
    t1.setpos(x,y)
    t1.setheading(0)
    for i in range(4):
        t1.forward(size) 
        t1.right(angle) 
 
def 3(): 
    t1.clear() 
    t1.setpos(200,0) 
    t1.circle(200) 
    ha((0,0),200) 
 
def keyup(): 
    pos=t1.pos() 
    t1.forward(45) 
    if rectangle((pos),[(0,-200),(200,0)]): 
        ((0,0),200) 
    if drawcircle((200,200),200,pos): 
        circle((200,0),200) 
 
def keyleft(): 
    t1.left(45) 
 
def keyright(): 
    t1.right(45) 
 
def keydown(): 
    pos=t1.pos() 
    t1.back(45) 
    if rectangle((pos),[(0,-200),(200,0)]): 
        1((0,0),200) 
    if drawcircle((200,200),200,pos): 
        circle((200,0),200) 
 
     
def keys(): 
    wn.onkey(keyup, "Up") 
    wn.onkey(keyleft, "Left") 
    wn.onkey(keyright, "Right") 
    wn.onkey(keydown, "Down") 
      
def mousegoto(x,y): 
    t1.setpos(x,y) 
    pos=t1.pos() 
    if rectangle((x,y),[(0,-200),(200,0)]): 
        1((0,0),200) 
    if drawcircle((200,200),200,pos): 
        circle((200,0),200) 
 
def mouse(): 
    wn.onclick(mousegoto) 
     
def game(): 
    3() 
    Keys() 
    mouse() 
    wn.listen()
    turtle.mainloop() 
 
 
def lab11(): 
    game() 
 
lab11() 