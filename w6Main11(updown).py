def main():
    import random
    s1=random.randrange(1,100)
    global r1
    r1 = input('Take a guess')
    if (s1>r1):
        result = "up"
        print result
        main()
    elif (s1<r1):
        result = "down"
        print result
        main()
    else :
        result = "correct"
        print result