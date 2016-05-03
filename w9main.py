def CharCount():
    sentence="sangmyung university"
    allchars= list(sentence)
    
    d=dict()
    for c in allchars:
        if c not in d:
            d[c]=1
        else:
            d[c]=d[c]+1

    import matplotlib
    import matplotlib.pyplot as plt
    
    plt.bar(range(len(d)),d.values(), align='center')
    plt.bar(range(len(d)), list(d.keys()))
    plt.show()

def CountDigitsLetters():
    word="20, Hongjimun 2-gil, Jongno-gu, Seoul"
    allchars=list(word)
    d=dict()
    d['number']=0
    d['word']=0
    for c in allchars:
        if c.isdigit():
            d['number']=d['number']+1
        else:
            d['word']=d['word']+1
        
    import matplotlib
    import matplotlib.pyplot as plt
    
    plt.bar(range(len(d)),d.values(), align='center')
    plt.bar(range(len(d)), list(d.keys()))
    plt.show()

def FindDifference():
    myhome=set()
    yourhome=set()
    myhome=set(['TV', 'phone', 'camera', 'fridger', 'mixer', 'audio', 'cd player', 'light', 'computer', 'notebook', 'recorder'])
    yourhome=set(['coffee machine', 'radio', 'camera', 'running machine', 'ramp', 'computer', 'notebook', 'recorder'])
    print ("only myhome: " ,myhome)
    print ("only your home: " ,yourhome)
    print ("both: " ,myhome.intersection(yourhome))
    print ("all: " ,myhome.union(yourhome))
    print ("How many?: " ,len(myhome.union(yourhome)))
    
    
def lab8():
    CharCount()
    CountDigitsLetters()
    FindDifference()
    
def main():
    lab8()
    
if __name__=="__main__":
    main()