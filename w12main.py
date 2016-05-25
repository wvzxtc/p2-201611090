import os 
mydir=os.getcwd() 
 
def 1(): 
    filename=raw_input("filename(ex:python.txt):") 
    myfilename=os.path.join(mydir,filename) 
    try: 
        myfile=open(myfilename, 'r') 
        contents=myfile.readlines() 
        for i in range(0,len(contents)): 
            if contents[i].find('Python') >= 0: 
                print contents[i] 
        myfile.close() 
    except IOError as e: 
        print e 
 
def 2(): 
    filetwo=open('output.txt', 'w') 
    line1='first line\n' 
    filetwo.write(line1) 
    line2='second line\n' 
    filetwo.write(line2) 
    line3='third line' 
    filetwo.write(line3) 
    filetwo.close() 
    myfiletwo=open('output.txt', 'r') 
    contentstwo=myfiletwo.readlines() 
    for a in range(0,len(contentstwo)): 
        if contentstwo[a].find('l') >= 0: 
            result = contentstwo[a].split() 
        for b in range(0,len(result)): 
            if result[b].find('l') >= 0: 
                print result[b].upper() 
    myfiletwo.close() 
     
def lab(): 
    print "1" 
    1() 
    print "2" 
    2() 
 
def main(): 
    lab() 
    raw_input() 
 
if __name__=="__main__": 
    main() 