import sys
from collections import deque
r=sys.stdin.readline
tn=int(r().rstrip())
for _ in range(tn):
    ar=[]
    result=0

    n=int(r().rstrip())
    visit=[0]*n
    for _ in range(n):
        a,b=map(int,r().rstrip().split())
        ar.append([a,b])
    ar.sort(key=lambda x:(x[0]))
    m=1000000
    for i in range(len(ar)):
        if ar[i][1] >m:
            continue
        else:
            m=ar[i][1]
            result+=1


    print(result)