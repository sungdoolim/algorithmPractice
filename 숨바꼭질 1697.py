from collections import deque
start,m=map(int,(input().split()))
M=100001
ar=[-1]*M
q=deque([])
ar[start]=0
q.append(start)
def bfs():
    while q:
        s=q.popleft()
        if ar[m]!=-1:
            return 0
        if s-1>=0 and ar[s-1]==-1:
            q.append(s-1)
            ar[s-1]=ar[s]+1
        if s+1<M and ar[s+1]==-1:
            q.append(s+1)
            ar[s+1]=ar[s]+1
        if s*2<M and ar[s*2]==-1:
            q.append(s*2)
            ar[s*2]=ar[s]+1
        
bfs()
print(ar[m])