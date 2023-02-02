print("generator using yield keyword")
def simple():
    for i in range(10):
        if(i%2==0):
            yield i
for i in simple():
    print(i)    

print("\n use multiple yield statement")
def multiple_yield():
    str1="first string"
    yield str1
    str2="second string"
    yield str2
    str3="third string"
    yield str3

obj=multiple_yield()
print(next(obj))
print(next(obj))
print(next(obj))