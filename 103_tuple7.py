print("chainging a tuple")

t="tuple","python","order","immutable",[1,2,3,4]
try:
    t[2]="item"
    print(t)
except Exception as e:
    print(e)
t[-1][2]=10
print(t)
t=("python","item")
print(t)        

print(t+(4,5,6))