from array import*
num=array('H',[1,2,3,4,5,6,2,2])
print(num.typecode)
print(num.itemsize)
num.append(100)
print(num)
print(num.buffer_info())
print(num.count(2))
num.extend(num)
print("extended array=",(num))

