print("removing list element")
l2=[0,1,2,3,4]
print("printing the original list")
for i in l2:
    print(i,end=" ")
l2.remove(2)
print("\n printing list after removng first element ")
for i in l2:
    print(i,end=" ")   

print("\n to delete duplicate element of the list")

list=[1,2,2,3,4,5,6,5,5,3]
list2=[]
for i in list:
  if i not in list2:
    list2.append(i)
print(list2)

print("\n to find sum of element in list")
sum=0
for i in list2:
    sum=sum+i
print("the sum is=",sum)    
       
print("\n to find at least 1 common element")
l3=[10,20,30,50,49]
l4=[60,70,80,49,90]

for x in l3:
   for y in l4:
       if x==y:
        print("the common element is=",x)        