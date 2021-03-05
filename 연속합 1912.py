import sys
r=sys.stdin.readline
n=int(r().rstrip())
ar=list(map(int,r().rstrip().split()))
dp=[0]*n

dp[0]=ar[0]
for i in range(1,n):
    dp[i]=max(dp[i-1]+ar[i],ar[i])
#print(dp)


print(max(dp))
