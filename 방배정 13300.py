
import math
n,k=map(int,input().split())
girls=[0]*7
boys=[0]*7

for _ in range(n):
    a,b=map(int,input().split())
    if a==0:
        girls[b]+=1
    else:
        boys[b]+=1
sum=0
for i in range(7):
    sum+=(math.ceil(girls[i]/k)+math.ceil(boys[i]/k))
print(sum)


