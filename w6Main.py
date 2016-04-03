Python 2.7.11 |Anaconda 2.5.0 (32-bit)| (default, Jan 29 2016, 15:36:56) [MSC v.
1500 32 bit (Intel)]
Type "copyright", "credits" or "license" for more information.

IPython 4.0.3 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.

In [1]: def main():
   ...:     print "Let's play R S P game!!"
   ...:     p1=raw_input("hey first guy what's your choice? please input only be
tween r s p: ")
   ...:     p2=raw_input("how about you,next guy: ")
   ...:

In [2]: def subtool(p):
   ...:     if(p=='r'):
   ...:         return 1.0
   ...:     elif(p=='s'):
   ...:         return 2.0
   ...:     elif(p=='p'):
   ...:         return 4.0
   ...:     else:
   ...:         print "Input Error"
   ...:         alpha=subtool(p1)/subtool(p2)
   ...:     if(alpha==0.5):
   ...:         print "p1 you win!!"
   ...:     elif(alpha==1):
   ...:         print "draw :)"
   ...:     elif(alpha==0.25):
   ...:         print "p2 you win!!"
   ...:     elif(alpha==2):
   ...:         print "p2 you win!!"
   ...:     elif(alpha==4):
   ...:         print "p1 you win!!"
   ...:

In [3]: main()
Let's play R S P game!!
hey first guy what's your choice? please input only between r s p:
how about you,next guy:

In [4]: wn.exitonclick()
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-4-06fc7d45910f> in <module>()
----> 1 wn.exitonclick()

NameError: name 'wn' is not defined

In [5]: %history
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
%history

In [6]: wn.exitonclick()