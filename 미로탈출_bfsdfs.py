n,m=map(int,input().split())
graph=[]
for _ in range(n):
    graph.append(list(map(int,input())))
print(graph)
def boundint(i,j):
    if i>=n or i<0 or j<0 or j>=m:
        return False;
    else:
        return True;
result=[]
def dfs(i,j):
    if boundint(i,j) :
        if boundint(i+1,j) and graph[i+1][j]==1:
            graph[i+1][j]+=graph[i][j]
            dfs(i+1,j)
        if boundint(i-1,j)and graph[i-1][j]==1:
            graph[i-1][j]+=graph[i][j]
            dfs(i-1,j)
        if boundint(i,j-1)and graph[i][j-1]==1:
            graph[i][j-1]+=graph[i][j]
            dfs(i,j-1)
        if boundint(i,j+1)and graph[i][j+1]==1:
            graph[i][j+1]+=graph[i][j]
            dfs(i,j+1)
        

    else:
        return 0

print(dfs(0,0))
print(graph[n-1][m-1])

'''
5 6
101010
111111
000001
111111
111111
'''
        