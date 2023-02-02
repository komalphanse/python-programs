l=[x for x in range(4)]
print(l)

d1={var:var+3 for var in l}
print(d1)

print("example2")
l1=[x for x in range(7)]
l2=["sunday","monday","tuesday","wednday","thursday","friday","saturday"]
print(l1)
print(l2)
new_dict={key:value for (key,value) in zip(l1,l2)}
print(new_dict)