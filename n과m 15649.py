from itertools import permutations
a,b=map(int,input().split())
ar=[i for i in range(1,a+1)]
#print(ar)
result=list(permutations(ar,b))

for k in result:
    for j in k:
        print(j,end=" ")
    print()
