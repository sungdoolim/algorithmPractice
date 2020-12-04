from itertools import combinations
a,b=map(int,input().split())
ar=[i for i in range(1,a+1)]
#print(ar)
result=list(combinations(ar,b))

for k in result:
    for j in k:
        print(j,end=" ")
    print()
