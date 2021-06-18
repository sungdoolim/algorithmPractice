import sys

global n,m
n,m,p=map(int,sys.stdin.readline().rstrip().split())
ar=[[1]*m for _ in range(n)]



def dps(sx,sy,x,y):

    for i in range(sx+1,x):
        for j in range(sy+1,y):
            ar[i][j]=ar[i-1][j]+ar[i][j-1]
    return ar[-1][-1]   
def dp(x,y):

    v=0
    dps(0,0,x+1,y+1)
    X=ar[x][y]
    ar[x][y]=1
    dps(x,y,n,m)
    Y=ar[-1][-1]
    print(X*Y)

if p!=0:
    q=p//m
    r=p%m
    if r==0:
        q-=1
        r=m-1
        ar[q][r]=1
    else:
        r=r-1
        ar[q][r]=1

    dp(q,r)

else:

    print(dps(0,0,n,m))

