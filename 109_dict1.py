emp={"name":"pournima","age":27,"company":"tech mahindra","salary":25000}
print(type(emp))
print(emp)
print("printing employee data...")

print("name:",emp["name"])
print("age:",emp["age"])
print("company:%s"%emp["company"])
print("salary",emp["salary"])
print("\nEnter the detail of new employee...")
emp["name"]=input("name=")
emp["age"]=int(input("Age="))
emp["company"]=input("company=")
emp["salary"]=int(input("salary="))
print("printing the new data",emp)

