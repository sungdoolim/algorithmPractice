import sys
readli=sys.stdin.readline
tn=int(readli().rstrip())
result=[]
global ar,ckl,count
ar=[]
ckl=[]
count=0
def dfs(i,j):
    if i>=a or i<0 or j>=b or j<0 or ckl[i][j]==1 or ar[i][j]==0:
        return False
    else:
        ckl[i][j]=1
        dfs(i+1,j)
        dfs(i-1,j)
        dfs(i,j+1)
        dfs(i,j-1)

        return True

for _ in range(tn):
    a,b,c=map(int,readli().rstrip().split())
    ar=[[0]*(b) for _ in range(a)]
    ckl=[[0]*(b) for _ in range(a)]
    
   # print(ar)
    for _ in range(c):
        x,y=map(int,readli().rstrip().split())
        ar[x][y]=1
    #print(ar)
    count=0
    for i in range(a):
        for j in range(b):
            if dfs(i,j):
                count+=1
            #print(count)
    result.append(count)
    
for i in result:
    print(i)