from ast import arguments


# arbitory arguments
def my_function(*kids):
    print("the youngest child is" + " "+kids[2])
my_function("emil","tobies","linus")    