import sys
n,m=map(int,sys.stdin.readline().rstrip().split())
graph=[[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,sys.stdin.readline().rstrip().split())
    graph[a][b]=1
    graph[b][a]=1
# for i in graph:
#     print(i)
#print()
count=0
ckl=[0]*(n+1)
stac=[]
def dfs(i):
    if ckl[i]==1:
        return False;
    else:
        ckl[i]=1
        for k in range(n,0,-1):
            if ckl[k]==0 and k not in stac and graph[i][k]==1:
                
                stac.append(k)
        #print(stac)
        if stac:
            dfs(stac.pop())
        return True

for j in range(1,n+1):
    if dfs(j):
        #print(ckl)
        count+=1
print(count)

