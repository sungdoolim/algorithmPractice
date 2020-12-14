from itertools import combinations_with_replacement
a,b=map(int,input().split())
ar=[i for i in range(1,a+1)]
#print(ar)
result=list(combinations_with_replacement(ar,b))

for k in result:
    for j in k:
        print(j,end=" ")
    print()
