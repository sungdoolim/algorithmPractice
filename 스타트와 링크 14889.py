from itertools import combinations
from itertools import permutations

n=int(input())
br=[i for i in range(n)]
#print(br)
ar=[]
for _ in range(n):
    ar.append(list(map(int,input().split())))
#print(ar)
cr=list(combinations(br,n//2))  
cl=len(cr)
round=cl//2
#print(cr) 
#print(cl)
cha=0
result=[]
for i in range(round):
    #cr[i] cr[cl-i-1]

    sumone=0
    sumtwo=0
    oneper=list(permutations(cr[i],2))
    #print(oneper)
    for j in oneper:
     #   print(j[0],j[1])
        sumone+=ar[j[0]][j[1]]
    
    
    twoper=list(permutations(cr[cl-i-1],2))
    for j in twoper:
        sumtwo+=ar[j[0]][j[1]]
    result.append(abs(sumone-sumtwo))
#print(result)
print(min(result))


