﻿x=list()

def totalList(x):
    x=list()
    for i in range(1,1000):
            if i%4==0 and not i%5==0:
                x.append(i) 
    sum=0
    for i in range(0,len(x)):
        sum+=x[i]
    return sum

totalList(x)

def lab6():
    print """happy programming!"""
    labtotal=totalList(x)
    print labtotal
    
def main():
    lab6()
    
if __name__=="__main__":  
      main()  
