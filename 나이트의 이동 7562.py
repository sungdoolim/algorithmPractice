from collections import deque
tn=int(input())
x=[-1,-1,1,1,-2,-2,2,2]
y=[2,-2,2,-2,1,-1,1,-1]
count=0
def bfs(i,j):
    global x1,y1,bound,count
    q=deque()
    q.append([i,j])
    ar[i][j]=1
    while q:
        i,j=q.popleft()
        if i==x1 and j==y1:
            print(ar[i][j]-1)
            break
        else:
            for k in range(8):
                tmpi=i+x[k]
                tmpj=j+y[k]
                if tmpi>=bound or tmpj>=bound or tmpi<0 or tmpj<0 or ar[tmpi][tmpj]!=0:
                    continue
                    
                q.append([tmpi,tmpj])
                ar[tmpi][tmpj]=ar[i][j]+1


for _ in range(tn):
    
    bound=int(input())
    x0,y0=map(int,input().split())
    x1,y1=map(int,input().split())
    ar=[[0]*bound for _ in range(bound)]
    bfs(x0,y0)