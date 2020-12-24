import sys
n=int(sys.stdin.readline().rstrip())
ar=[]
ckl=[[0]*n for _ in range(n)]
for _ in range(n):
    ar.append(list(map(int,input())))
k=0
def dfs(i,j):
    global k
    if i<0 or j<0 or i>=n or j>=n or ckl[i][j]==1 or ar[i][j]==0:
        return False
        
    else:
        k+=1
        ckl[i][j]=1
        dfs(i+1,j)
        dfs(i-1,j)
        dfs(i,j+1)
        dfs(i,j-1)
               



        return True
count=0
result=[]
for i in range(n):
    for j in range(n):
        k=0
        if(dfs(i,j)):
            count+=1
            result.append(k)
# print(ar)
# print(ckl)
result.sort()
print(count)
for i in result:
    print(i)
