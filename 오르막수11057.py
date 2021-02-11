n=int(input())
dp=[[1]*10 for _ in range(n)]
#print(dp)

for i in range(1,n):
    for j in range(1,10):
        dp[i][j]=dp[i-1][j]+dp[i][j-1]

print(sum(dp[n-1])%10007)


