from itertools import product
a,b=map(int,input().split())
ar=[i for i in range(1,a+1)]
#print(ar)
result=list(product(ar,repeat=b))

for k in result:
    for j in k:
        print(j,end=" ")
    print()
