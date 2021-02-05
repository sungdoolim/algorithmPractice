n=int(input())
result=[[0]* 10 for _ in range(n)]
result[0][0]=0
for i in range(1,10):
    result[0][i]=1
#print(result)

for i in range(1,n):
    for j in range(0,10):
 #       print(i,j)
        if j==0:
            result[i][j]=result[i-1][1]
        elif j==9:
            result[i][j]=result[i-1][8]
        else:
            result[i][j]=result[i-1][j-1]+result[i-1][j+1]

print(sum(result[n-1])%1000000000)
