from re import X

def decore1(func):
    def inner():
        x=func()
        return x*X
    return inner 
def decor(func):
    def inner():
        x=func()
        return 2*X
    return inner
@decore1
@decor
def num():
     return 10
print(num())     