def main():
    print "Let's play R S P game!!"
    p1=raw_input("hey first guy what's your choice? please input only between r
s p: ")
    p2=raw_input("how about you,next guy: ")
def subtool(p):
    if(p=='r'):
        return 1.0
    elif(p=='s'):
        return 2.0
    elif(p=='p'):
        return 4.0
    else:
        print "Input Error"
        alpha=subtool(p1)/subtool(p2)
    if(alpha==0.5):
        print "p1 you win!!"
    elif(alpha==1):
        print "draw :)"
    elif(alpha==0.25):
        print "p2 you win!!"
    elif(alpha==2):
        print "p2 you win!!"
    elif(alpha==4):
        print "p1 you win!!"
main()
wn.exitonclick()