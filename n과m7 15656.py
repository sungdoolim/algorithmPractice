from itertools import product
n,m=map(int,input().split())
data=list(map(int,input().split()))
result=list(product(data,repeat=m))
result.sort()
print(result)
for i in result:
    for j in i:
        print(j,end=" ")
    print()
