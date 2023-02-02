from array import*
a1=array('i',[10,20,30])
b=a1.tobytes()
print(b)
a1.frombytes(b)
print('a1=',a1)