import sys

start=2
count=1
n=int(sys.stdin.readline().rstrip())
square=[300000]*300001
square[0]=1
while True:
    count+=start
    square[start-1]=(square[start-2]+count)
    if square[start-1]>=n:
        break
    start+=1
#print(square)



dp=[1000000]*(n+1)
dp[0]=0
dp[1]=1
for j in range(2,n+1):
    for i in square:
        if j>=i:
            dp[j]=min(dp[j-i]+1,dp[j])
        else:
            break
# print(square)
# print(result)
print(dp[-1])


