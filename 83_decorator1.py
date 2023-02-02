#passing the function as an argument

def  shout(text):
    return text.upper()
def honda(text):
    return text.lower()
def greet(func):
    greeting=func("hi samu")
    print(greeting)        
greet(shout)

greet(honda)