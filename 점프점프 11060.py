n=int(input())
ar=list(map(int,input().split()))
#print(ar)
result=[10000]*(n+1)
result[0]=0

for i in range(n):
    for j in range(i+1,ar[i]+i+1):
        if j>=n:
            continue
        result[j]=min(result[j],result[i]+1)
 #       print(result)
#print(result)
if result[-2]!=10000:
    print(result[-2])
else:
    print(-1)
