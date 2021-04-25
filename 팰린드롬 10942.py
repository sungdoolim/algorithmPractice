import sys
r=sys.stdin.readline
n=int(r().rstrip())
ar=list(map(int,r().rstrip().split()))
m=int(input())
dpar=[[0]*n for _ in range(n)]
#print(dpar)

br=[]
for _ in range(m):
    br.append(list(map(int,r().rstrip().split())))
#print(ar,br)

def dp(i,j):
    if j-i==0:
        dpar[i][j]=1
    elif j-i==1:
        if ar[i]==ar[j]:
            dpar[i][j]=1
        else:
            dpar[i][j]=0
    else:
       # print(i,j,dpar[i+1][j-1])
        if ar[i]==ar[j] and dpar[i+1][j-1]:
            dpar[i][j]=1
        else:
            dpar[i][j]=0
count=0
while True:
    if count==n:
        break
    for i in range(n):
        j=i+count
        dp(i,j)
        if j==n-1:
            break
    count+=1
#print(dpar)
for j in br:
    print(dpar[j[0]-1][j[1]-1])
