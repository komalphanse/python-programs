per=float(input("enter percentage="))

if(per>=75):
    print("first class with distinction")
elif(per>=60 and per<=75):
    print("first class") 
elif(per>=50 and per<=60):
    print("second class")
elif(per>=35 and per<=50):
    print("pass")
else:
    print("fail")          