empty_tuple=0
int_tuple=4,6,8,10,12,14
print("tuple with integer",int_tuple)

mix_tuple=(4,"python",9.3)
print(mix_tuple)

nested_tuple=(4,"python",{4:5,6:2,8:2},(5,3,5,6))
print("nested tuple=",nested_tuple)
print(type(nested_tuple))

try :
      nested_tuple[1]=4.5
except :
         print(TypeError)       