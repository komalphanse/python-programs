def hello(func):

    def inner1():

        print("hello,this is before function execution")
        func()

        print ("This is after function exicution")

    return inner1

def function():

    print("This is inside function")

function=hello(function)
function()           