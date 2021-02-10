import math
l=int(input())
c=int(input())
ar=list(map(int,input().split()))


ar.sort()

m=2*ar[0]
for i in range(c-1):
    
    m=max(m,ar[i+1]-ar[i])
m=max(m,2*(l-ar[-1]))
#print(ar)  
print(math.ceil(m/2))