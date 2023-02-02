list=[1,2,3,4,5,6,7]
print("slicing list")
print(list[0])
print(list[1])
print(list[2])
print(list[0:6])
print(list[:])
print(list[2:5])

l1=[1,2,3,4,5]
print("\n negative indexing ")
print(l1[-1])
print(l1[-3:])
print(l1[:-1])
print(l1[-3:-1])

print("\n updating list")
print(list)
list[2]=10
print(list)
list[1:3]=[89,78]
print(list)
list[-1]=25
print(list)
list[3:6]=[7,8,9]
print(list)

print(list+l1)
print(l1*2)
print(2 in l1)

print("length of list:",len(list))

print("length of l1:",len(l1))

for i in l1:
    print(i)
