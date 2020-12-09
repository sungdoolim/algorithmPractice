import math

from bisect import bisect_left
from bisect import bisect_right
n=int(input())
nm=int(input())
m=10001
ar=[0]*m
br=[]
for i in range(2,int(math.sqrt(m)+1)):
    if ar[i]==1:
        continue
    else:
        j=2
        while i*j<m:
            ar[i*j]=1
            
            j+=1
for i in range(2,m):
    if ar[i]==0:
        br.append(i)
#print(ar)
#print(br)
a=bisect_left(br,n)
b=bisect_right(br,nm)
#print(br)
#print(a,b)
if a>=b:
    print(-1)
else:
    print(sum(br[a:b]))
    print(br[a])