def drawSquareAt(size, pos):
    t1.penup()
    t1.setpos(pos)
    t1.pendown()
    tracks=list()
    for i in range(0,4):
        tracks.append(t1,pos())
        t1.forward(size)
        t1.right(90)
    return tracks

def lab7a():
    size=100
    pos=t1.pos
    mytrack=drawSquareAt(size, pos)
    print mytrack
    
def main():
    lab7a()