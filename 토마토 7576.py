import sys
from collections import deque
que=deque()
n,m=map(int,sys.stdin.readline().rstrip().split())
ar=[]
for i in range(m):
    ar.append(list(map(int,sys.stdin.readline().rstrip().split())))

for i in range(m):
    for j in range(n):
        if ar[i][j]==1:
            que.append([i,j])
# for i in que:
#     print(i)
def trans(i,j):
    if i>=m or j>=n or i<0 or j<0 or ar[i][j]!=0:
        return False
    ar[i][j]=1
    que.append([i,j])
    return True
count=0
while que:
    count+=1
    for _ in range(len(que)):
        a,b=que.popleft()
        trans(a+1,b)
        trans(a-1,b)
        trans(a,b-1)
        trans(a,b+1)
# for i in ar:
#     print(i)
b=True
for i in ar:
    if 0 in i:
        print(-1)
        b=False
        break
if b:
    print(count-1)



# import sys
# from collections import deque
# que=deque()
# n,m=map(int,sys.stdin.readline().rstrip().split())
# ar=[]

# tmpc=0
# for i in range(m):
#     ar.append(list(map(int,sys.stdin.readline().rstrip().split())))
#     for j in range(n):
#         if ar[i][j]==1:
#             que.append([i,j])
#             tmpc+=1
# #print(ar)
# def check(i,j):
#     if i<0 or j<0 or i>=m or j>=n or ar[i][j]!=0:
#         return False
#     else:
#         ar[i][j]=1
#         que.append([i,j])   
#         return True
# count=-1
# def dfs(l):
#     global count
#     count+=1
#     #print(l)
#     tc=0
#     for _ in range(l):
#         i,j=que.popleft()
#      #   print(i,j)
#         if check(i+1,j): tc+=1
#         if check(i-1,j): tc+=1
#         if check(i,j-1): tc+=1
#         if check(i,j+1): tc+=1
#     if que:
#         dfs(tc)


# # tmpc=0
# # for i in range(m):
# #     for j in range(n):
# #         if ar[i][j]==1:
# #             que.append((i,j))
# #             tmpc+=1


# dfs(tmpc)
# #print(ar)
# def result():
#     for i in ar:
#         if 0 in i:
#             print(-1)
#             return
#     print(count)


# result()
