import sys
r=sys.stdin.readline
n,k=map(int,r().rstrip().split())
ar=[]
resultdp=[0]*(k+1)
resultdp[0]=1
for _ in range(n):
    ar.append(int(r().rstrip()))
#ar.sort()

for i in ar:
    print(resultdp)
    for j in range(i,k+1):
        if j-i>=0:
            resultdp[j]+=(resultdp[j-i])
        else:
            break
print(resultdp)