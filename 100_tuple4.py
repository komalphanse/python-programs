print("delet element in tuple")
t=("python","tuple","ordered","imutable","collection","object")

try:
    del t[3]
    print(t)
except Exception as e:
    print(e)

del t        
try:
    print(t)
except Exception as e:
    print(e)    

