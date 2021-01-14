n=int(input())
from bisect import bisect_right,bisect_left

ar=list(map(int,input().split()))
m=int(input())
br=list(map(int,input().split()))
#print(ar,br)
result=[]
ar.sort()

for i in br:
    a=bisect_right(ar,i)
    b=bisect_left(ar,i)
    result.append(a-b)

# for i in br:
#     count=0
#     for j in ar:
#         if i==j:
#             count+=1
#     result.append(count)
for i in result:
    print(i,end=" ")