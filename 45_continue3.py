number=[10,20,0,5,0,30]
for n in  number:
    if n ==0:
        print("hey how we can divide with zero just skipping")
 
        continue
    print("100/{}={}".format(n,100/n))