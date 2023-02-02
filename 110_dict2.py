print("create a dictiony using dict() method")
dict1=dict({1:"java",2:"t",3:"poinyt"})
print(dict1)

dict2=dict([(1,"devansh"),(2,"sharma")])
print(dict2)

print("\n Adding dictionary values")

dict3={}
print("empty dictionary=",dict3)
dict3[0]="peter"
dict3[2]="joseph"
dict3[3]="ricky"
print(dict3)
dict3["ages"]=20,33,24
print("\n after adding age=",dict3)


print("\n updating keys values")
dict3[3]="javapoint"
print(dict3)


print("\n deleting the data")
del dict3[2]
print(dict3)

print("delete the dictionry..")
del[dict3]
print("lets try to print it again",dict3)