my_t=("apple","banana","cherry")
a=iter(my_t)
print(next(a))
print(next(a))
print(next(a))

print("\nlooping through iterator")
for x in my_t:
    print(x)

print("\n string are also iterable object,containing sequence of character")
str="banana"
a=iter(str)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))











