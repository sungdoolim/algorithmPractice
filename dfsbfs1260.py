from collections import deque
import sys
n,m,s=map(int,sys.stdin.readline().rstrip().split())
graph=[[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,sys.stdin.readline().rstrip().split())
    graph[a][b]=1
    graph[b][a]=1
ckl=[0]*(n+1)

def dfs(s):
    global n
    #print(ckl)
    if ckl[s]==0:
        ckl[s]=1
        print(s,end=" ")
        for i in range(1,n+1):
      #      print(s,i,graph[s][i])
            if graph[s][i]==1:
                dfs(i)

dfs(s)
print()
ckl=[0]*(n+1)

q=deque()
q.append(s)
ckl[s]=1
def bfs():
    while q:
        a=q.popleft()
        print(a,end=" ")
        for i in range(1,n+1):
            if graph[a][i]==1 and ckl[i]==0:
                ckl[i]=1
                q.append(i)


bfs()







# from collections import deque
# import sys
# n,m,s=map(int,sys.stdin.readline().rstrip().split())
# graph=[[0]*(n+1) for _ in range(n+1)]
# #print(graph)
# for _ in range(m):
#     a,b=map(int,sys.stdin.readline().rstrip().split())
#     graph[a][b]=1
#     graph[b][a]=1

# # for k in graph:
# #     print(k)
# ckl=[]
# stac=[]
# que=deque([])
# def dfs(s):
#     if s in ckl:
#         return 0
#     else:
#         ckl.append(s)
#         for i in range(n,0,-1):
#             #print(i)
#             if graph[s][i]==1 and i not in ckl:
#                 stac.append(i)
#                 #print(stac)

#     if stac:
#         #print(stac)
#         dfs(stac.pop())


# def bfs(s):
#     if s in ckl:
#         return 0
#     else :
#         ckl.append(s)
        
#         for i in range(1,n+1):
#             if i not in ckl and graph[s][i]==1:
#                 que.append(i)
                
#         if que:
#             bfs(que.popleft())



# dfs(s)
# for i in ckl:
#     print(i,end=" ")
# print()

# ckl.clear()
# bfs(s)
# for i in ckl:
#     print(i,end=" ")
