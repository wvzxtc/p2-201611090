my2dlist=[
[74425,76326],
[61164,61636],
[109688,115744],
[144796,146776],
[174996,181676],
[177841,177434],
[204630,205980],
[223373,232245],
[161055,166130],
[171576,176735],
[279169,293772],
[239450,251066],
[148690,156510],
[182977,196992],
[237792,242641],
[283869,296762],
[209344,210282],
[118965,114441],
[186503,186856],
[195734,203014],
[254381,249472],
[212401,229111],
[271654,295354],
[319197,335045],
[229829,231671]]
total_m=0
total_w=0
for i in my2dlist:
    total_m=total_m+i[0]
print "남 합계:", total_m
for i in my2dlist:
    total_w=total_w+i[1]
print "여 합계:", total_w
    
average_m=total_m/25
print "남 평균:", average_m
average_w=total_w/25
print "여 평균:", average_w

total_gu=0
for i in my2dlist:
    total_gu=i[0]+i[1]
    print "구 합계:", total_gu
    
for i in my2dlist:
    average_gu=(i[0]+i[1])/2
    print "구 평균:", average_gu
    
my2dlist=tuple()
for i in my2dlist:
    my2dlist.append(i[0]+i[1])
    
%matplotlib inline
import matplotlib
import matplotlib.pyplot as plt
plt.bar(range(0,len(my2dlist)),my2dlist, align='center')
plt.show()

plt.show()