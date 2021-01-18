n=int(input())
ar=[1,5,10,50]
from itertools import combinations_with_replacement
result=list(combinations_with_replacement(ar,n))
#print(result)
R=[]
for i in result:
    R.append(sum(i))
R=set(R)
print(len(R))