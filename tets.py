
import time

def rec(n):
    
    if n==0:
        print('done')
        return
    print(n)
    time.sleep(3)
    n -= 1
    rec(n)

#rec(6)

list12=[1,2,4]
k=0
for i in list12:
    k=i+k
print(k)


def rec2(x):
    if len(x)==1:
        return x[0]
    
    return x[0]+rec2(x[1:])
print(rec2(list12))

