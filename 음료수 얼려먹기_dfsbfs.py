n,m=map(int,input().split())
graph=[]
for _ in range(n):
    graph.append(list(map(int,input())))
print(graph)

def dfs(i,j):
    if i>=n or i<0 or j>=m or j<0:
        return False
    if graph[i][j]==0 :
        graph[i][j]=1
        dfs(i+1,j)
        dfs(i-1,j)
        dfs(i,j+1)
        dfs(i,j-1)

        return True
    else:
        return False

count=0
for i in range (n):
    for j in range(m):
        if dfs(i,j):
            count+=1
print(count)
'''
4 5
00110
00011
11111
00000
'''