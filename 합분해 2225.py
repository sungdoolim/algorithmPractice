n,k=map(int,input().split())
result=[[1]*k for _ in range(n)]

for i in range(k):
    result[0][i]=i+1

for i in range(1,n):
    for j in range(1,k):
        result[i][j]=result[i-1][j]+result[i][j-1]
print(result[n-1][k-1]%1000000000)