import sys
from collections import deque
n,m=map(int,sys.stdin.readline().rstrip().split())
ar=[]
que=deque([(0,0,0)])
#print(ar)
for _ in range(n):
    ar.append(list(map(int,input())))
ckl=[[0]*m for _ in range(n)]
#print(ckl)

def dfs():
    while que:
        i,j,c=que.popleft()
        #print(i,j,c)
        if i<0 or j <0 or i>=n or j>=m or ckl[i][j]!=0 or ar[i][j]==0:
            continue
        else:
            #c=ckl[i][j]
            ckl[i][j]=c+1
            que.append((i+1,j,c+1))
            que.append((i-1,j,c+1))
            que.append((i,j+1,c+1))
            que.append((i,j-1,c+1))
            
            


dfs()
#print(ar)
#print(ckl)
print(ckl[n-1][m-1])