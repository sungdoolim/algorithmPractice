from math import gcd
import sys
r=sys.stdin.readline
def lcm(a,b):
    return a*b//(gcd(a,b))
n=int(r().rstrip())


ar=[]
for _ in range(n):
    ar.append(list(map(int,r().rstrip().split())))
result=[]
for tmp in ar:
    a,b,c,d=tmp[0],tmp[1],tmp[2],tmp[3]
    arr=[]
    arr.append(c)
    brr=[]
    brr.append(d)
    g=lcm(a,b)
    #print(g)
    i=1
    j=1
    while True:
        ta=a*i+c
        arr.append(ta)
        tb=b*i+d
        brr.append(tb)
        i+=1
        if ta>g and tb>g:
            break


    crr=set(arr)&set(brr)
    if crr:
        print(min(crr))
    else:
        print(-1)

