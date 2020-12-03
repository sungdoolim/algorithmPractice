import sys
from collections import deque
n,m,k,x=map(int,sys.stdin.readline().rstrip().split())

graph=[[] for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,sys.stdin.readline().rstrip().split())
    graph[a].append(b)
arx=deque([x])
arx.append(x)
result=[0]*(n+1)
result[x]=0

def bfs():
    #print(ckl)
    while arx:
        start=arx.popleft()
        for i in graph[start]:
            if result[i]==0:
                result[i]=result[start]+1
                arx.append(i)

bfs()
#print(result)
check=False
#print(result)
for i in range(1,n+1):
    if result[i]==k:
        print(i)
        check=True
if check==False:
    print(-1)