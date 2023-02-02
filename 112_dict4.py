emp={"name":"pournima","age":27,"company":"tech mahindra","salary":25000}
print(type(emp))
print(emp)
print("\n print all keys of dictionary")
for i in emp:
    print(i)

print("print all the values of dictionry")
for x in emp:
    print(emp[x])

for x in emp.values():
    print(x)    

print("print the items of dictionary using items() method")
for x in emp.items():
    print(x)    
for x,y in emp.items():

     print(x,y)