import math
Location=tuple()
MyList=list()
(x1,y1)=(37.575719, 126.973612)
Location=[(37.571605, 126.976604), (37.570193, 126.983031), (37.576499, 126.985386), (37.574510, 126.957592), (37.570443, 126.992115)]
for i in Location:
    MyList.append (math.sqrt((x1-i[0])**2+(y1-i[1])**2))
print min(MyList)