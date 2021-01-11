import sys

def dfs(i,j):
    global n,m
    #print(i,j)
    if i<0 or j<0 or i>=m or j>=n or ckl[i][j]==1 or ar[i][j]==0:
        return False
    else:
        ckl[i][j]=1
        dfs(i+1,j)
        dfs(i-1,j)
        dfs(i+1,j+1)
        dfs(i-1,j+1)
        dfs(i+1,j-1)
        dfs(i-1,j-1)
        dfs(i,j+1)
        dfs(i,j-1)
        return True

    

result=[]
while True:
    n,m=map(int,sys.stdin.readline().rstrip().split())
    
    if n==0 and m==0:
        break;
    else:
        count=0
        ar=[]
        ckl=[[0]*n for _ in range(m)]
        #print(ckl)
        for _ in range(m):
            ar.append(list(map(int,sys.stdin.readline().rstrip().split())))
        #print(ar)
        for i in range(m):
            for j in range(n):
                if dfs(i,j):
                    count+=1
        result.append(count)
        #print(count)
for k in result:
    print(k)
