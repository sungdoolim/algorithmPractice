n=int(input())
from collections import deque
for _ in range(n):
    a,b=map(int,input().split())
    count=1
    ar=list(map(int,input().split()))
    seq=deque([i for i in range(a)])

    
    #findr=ar[b]
    while True:
        
        tmp=seq.popleft()
        #print(seq)
        if seq and ar[tmp]<max(ar):
            seq.append(tmp)
            
        elif tmp==b:
            print(count)
            break
        else:
            ar[tmp]=-1
            count+=1
            continue


