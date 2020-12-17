import sys
from itertools import combinations
rl=sys.stdin.readline
n,m=map(int,rl().rstrip().split())
ar=list(map(int,rl().rstrip().split()))
ar.sort()
result=list(combinations(ar,m))
#print(result)
for i in result:
    for j in i:
        print(j,end=" ")
    print()
