height = input("Put in your height : ")
weight = input("Put in your weight : ")
BMI = weight * 10000 / (height * height)
print BMI
if BMI <= 18.5 :
    print "Underweight"
elif BMI > 18.5 and BMI <= 23 :
    print "Normalweight"
elif BMI > 23 and BMI <= 25 :
    print "Overweight"
elif BMI > 25 and BMI <= 30 :
    print "Obesity"
elif BMI > 30 :
    print "An extremely obese"
else :
    print "Input error"