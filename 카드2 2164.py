n=int(input())
from collections import deque
q=deque([i for i in range(1,n+1)])
#print(q)
while q:
    tmp=q.popleft()
    if q:
        q.append(q.popleft())
    else:
        print(tmp)