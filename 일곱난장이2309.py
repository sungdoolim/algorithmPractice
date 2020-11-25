# ar=[]
# for _ in range(9):
#     ar.append(int(input()))
# ar.sort()
# #print(ar)
# s=sum(ar)
# def two():
#     for i in range(9):
#         for j in range(9):
#             if i==j:
#                 continue;
#             else:
#                 k=ar[i]+ar[j]
#                 if s-k==100:
#                     for l in range(9):
#                         if l!=i and l!=j:
#                             print(ar[l])
#                     return 1;
# two()


# 여기는 combinations쓴거
from itertools import permutations
from itertools import combinations
ar=[]
for _ in range(9):
    ar.append(int(input()))
ar.sort()
#print(ar)
s=sum(ar)
case=list(combinations(ar,7))
for c in case:
    if sum(c)==100:
        for i in c:
            print(i)
        break;
