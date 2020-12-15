from itertools import permutations
n,m=map(int,input().split())
ar=[]

ar=list(map(int,input().split()))
ar.sort()
#print(ar)
result=list(permutations(ar,m))
for k in result:
    for j in k:
        print(j,end=" ")
    print()
