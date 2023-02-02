def hello(func):
    def inner1(*args,**kwargs):

        print("before exicution")

        value=func(*args,**kwargs)

        print("after exicution")

        return value

    return inner1    
#@hello

def sum(x,y):

    print("inside the function")
    return x+y
x,y=1,2
sum=hello(sum)
print("sum=",sum(x,y))