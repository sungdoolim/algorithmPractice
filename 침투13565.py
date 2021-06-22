n,m=map(int,input().split())
ar=[]
for _ in range(n):
    ar.append(list(map(int,input())))
stack=[]
ckl=[[0]*m for _ in range(n)]
#print(ckl)

def dfs():
    while stack:
        tmp=stack.pop()
        i=tmp[0]
        j=tmp[1]
       
        #print(i,j)
        if i<0 or i>=n or j<0 or j>=m or ar[i][j]==1 or ckl[i][j]==1:
           # 범위를 벗어나면 continue
           # 전류가 통하지 않거나, 이미 체크한 곳 이면 continue
            continue
        elif i==n-1:
            # inner side에 도착한 경우 True
            return True
        # 위 경우가 아니라면 4방에 대해 stack에 저장하고, 
        # 지금의 좌표는 중복체크 방지를 위해 ckl에 저장합니다.
        ckl[i][j]=1
        stack.append((i+1,j))
        stack.append((i,j+1))
        stack.append((i-1,j))
        stack.append((i,j-1))



#print(stack)
for i in range(m):
    # 가장 첫줄 중에 전류가 시작 될 좌표를 stack에 저장합니다
    if ar[0][i]==0:
        stack.append((0,i))


if(dfs()):
    print("YES")
else:
    print("NO")
#print(ar)
