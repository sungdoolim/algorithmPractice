import sys
from collections import deque
n,m=map(int,sys.stdin.readline().rstrip().split())
ar=[]
que=deque([(0,0,0)])
for _ in range(n):
    ar.append(list(map(int,input())))
result=[[0]*m for _ in range(n)]
def dfs():
    while que:
        i,j,c=que.popleft()

        if i<0 or j <0 or i>=n or j>=m or result[i][j]!=0 or ar[i][j]==0:
            continue
        else:
            result[i][j]=c+1
            que.append((i+1,j,c+1))
            que.append((i-1,j,c+1))
            que.append((i,j+1,c+1))
            que.append((i,j-1,c+1))

dfs()
print(result[n-1][m-1])