import sys


n=int(sys.stdin.readline().rstrip())
ar=[]
for i in range(n) :
    ar.append(list(map(int,sys.stdin.readline().rstrip().split())))

for i in range(n):
    print(ar[i][0]+ar[i][1])


