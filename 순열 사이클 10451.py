import sys

tn=int(sys.stdin.readline().rstrip())
def dfs(s,n):
    if ckl[s]==1:
        return True
    ckl[s]=1
    for i in range(n):
        
        if graph[s][i]==1 and ckl[i]==1:
            return False
        elif ckl[i]==0 and graph[s][i]==1:
            #graph[i][s]=0
            if not dfs(i,n):
                return False

    return True




for _ in range(tn):
    n=int(sys.stdin.readline().rstrip())
    graph=[[0]*n for _ in range(n)]
    
    ar=list(map(int,sys.stdin.readline().rstrip().split()))
    ckl=[0]*n
    for i in range(len(ar)):
        graph[i][ar[i]-1]=1
        #graph[ar[i]-1][i]=1
    # for i in graph:
    #     print(i)
    count=0
    for i in range(n):
        if not dfs(i,n):
            count+=1
        
    print(count)
    # for i in graph:
    #     print(i)
    