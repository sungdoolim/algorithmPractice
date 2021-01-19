n=int(input())
m=int(input())
ar=[]
br=[[0]*(n+1) for _ in range(n+1)]
ckl=[0]*(n+1)
stac=[1]
for _ in range(m):
    a,b=map(int,input().split())
    br[a][b]=1
    br[b][a]=1
for i in ar:
    print(i)

def dfs():
    while stac:
        a=stac.pop()    
        ckl[a]=1
        for i in range(n+1):
            if br[a][i]==1 and ckl[i]==0:
                stac.append(i)
dfs()
print(sum(ckl)-1)