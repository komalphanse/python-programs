print("show how to access tuple element")
t=("python","tuple","ordered","collection")
print(t[0])
print(t[1])
try :
    print(t[5])
except Exception as e:
    print(e)
try :
    print(t[1.0])
except Exception as e:
    print(e)

nested_t="tuple",[4,6,2,4],(6,2,6,7)
print(nested_t[0][3])
print(nested_t[1][1])    