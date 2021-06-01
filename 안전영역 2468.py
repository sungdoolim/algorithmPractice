import sys
from collections import deque
r=sys.stdin.readline
n=int(r().rstrip())
ar=[]
for _ in range(n):
    ar.append(list(map(int,r().rstrip().split())))



q=deque()
result=[0]*101
def bfs(i,j):
    global h,n
    b=False

    
    if ckl[i][j]==1:
        return b
    q.append([i,j])
    while q:
        i,j=q.popleft()
        #print(i,j)
        if i<0 or j<0 or i>=n or j>=n or ckl[i][j]==1:
            continue
        else  :
                ckl[i][j]=1

        
        if ar[i][j]>h:
            b=True
            
            q.append([i+1,j])
            q.append([i-1,j])
            q.append([i,j-1])
            q.append([i,j+1])


    return b


    

for h in range(100):
    count=0
    ckl=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if bfs(i,j):
                count+=1
    result[h]=count
print(max(result))





