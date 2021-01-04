from itertools import combinations
n,k=map(int,input().split())
ar=list(map(int,input().split()))
#print(ar)
count=0
for i in range(1,n+1):
    comb=list(combinations(ar,i))
    for j in comb:
        #print(sum(j))
        if sum(j)==k:
            count+=1
print(count)