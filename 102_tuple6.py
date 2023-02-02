print("membership test for tuple")

t=("python","tuple","ordered","immutable","collection","ordered")
print("tuple"in t)
print('Item'in t)
print('immutable' not in t)
print('item'not in t )
print("\n itteration using for loop")
for item in t:
    print(item)