import sys
r=sys.stdin.readline
n=int(r().rstrip())
ar=[]
result=[[0]*n for _ in range(n)]
for _ in range(n):
    ar.append(list(map(int,r().rstrip().split())))
# for i in ar:
#     print(i)

for i in range(n):
    q=[]
    ckl=[0]*(n+1)
    for j in range(n):
        
        if ar[i][j]==1:
            q.append(j)
    while q:
        k=q.pop()
        if ckl[k]==1:
            continue
        ckl[k]=1
        for l in range(n):
            if ar[k][l]==1:
                q.append(l)
    for x in range(n):
      #  print(i,x)
        if ckl[x]==1:
            result[i][x]=1
for i in result:
    for j in i:
        print(j,end=" ")
    print()

