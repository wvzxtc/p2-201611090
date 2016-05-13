Data = [('content', 13.1, 37.1, 8.7, 1.5),
('method', 10.6, 34.6, 13.4, 1.9),
('strelation', 27.1, 40.0, 2.9, 1.5),
('prrelation', 16.2, 37.8, 6.8, 0.8),
('equipment', 11.4, 29.8, 14.8, 4.9),
('enviroment', 12.2, 26.5, 14.9, 4.4),
('subject', 13.5, 29.7, 11.1, 2.4),
('school', 13.7, 37.6, 4.1, 1.2)]

def data():
    best=list()
    for i in range(0,len(Data)):
        best.append(Data[i][1])
    good=list()
    for i in range(0,len(Data)):
        good.append(Data[i][2])
    bad=list()
    for i in range(0,len(Data)):
        bad.append(Data[i][3])
    worst=list()
    for i in range(0,len(Data)):
        worst.append(Data[i][4])
    totalbest=0
    for i in range(0,len(Data)):
        totalbest = totalbest + best[i]
    totalgood = 0
    for i in range(0,len(Data)):
        totalgood = totalgood + good[i]
    goodtotal = 0
    goodtotal = totalbest + totalgood
    print "Best & good sum is ", goodtotal
    average = 0
    average_good = goodtotal / len(Data)
    print "Best & good average is ", average_good

    totalbad=0
    for i in range(0,len(Data)):
        totalbad = totalbad + bad[i]
    totalworst = 0
    for i in range(0,len(Data)):
        totalworst = totalworst + worst[i]
    badtotal = 0
    badtotal = totalbad + totalworst
    print "Bad & Worst sum is ", badtotal

    average_bad = 0
    average_bad = badtotal / len(Data)
    print "Bad & Worst average is ", average_bad

data()
raw_input("201611090")