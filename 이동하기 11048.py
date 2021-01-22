n,m=map(int,input().split())
ar=[]

for _ in range(n):
    ar.append(list(map(int,input().split())))
result=[[0]*m for _ in range(n)]
#print(ar)
#print(result)

def dp(i,j):
    if i-1>=0 and j-1>=0:
        result[i][j]=max(result[i-1][j],result[i][j],result[i][j-1])+ar[i][j]
    elif i-1>=0 and j-1<0:
        result[i][j]=max(result[i-1][j],result[i][j])+ar[i][j]
    elif i-1<0 and j-1>=0:
        result[i][j]=max(result[i][j],result[i][j-1])+ar[i][j]
    
    else:
        result[i][j]=ar[i][j]
    #dp(i+1,j+1,result[i][j])

for i in range(n):
    for j in range(m):
        dp(i,j)
# for i in result:
#     print(i)
print(result[n-1][m-1])
