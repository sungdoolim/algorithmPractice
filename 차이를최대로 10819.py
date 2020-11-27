from itertools import permutations
n=input()
ar=list(map(int,input().split()))
per=list(permutations(ar,int(n)))
result=[]

for i in per:
    sum=0
    for j in range(len(i)-1):
        sum+=abs(i[j]-i[j+1])
    result.append(sum)
print(max(result))