from itertools import permutations
num=[0,1,2,3,4,5,6,7,8,9]
n=int(input())
ar=input().split()
candidate=list(permutations(num,n+1))
#print(candidate)
result=[]
for i in candidate:
    j=0
    b=True
    for k in ar:
        if k==">":
            if i[j]>i[j+1]:
                j+=1
                pass
            else:
                b=False
                break
        else:
            if i[j]<i[j+1]:
                j+=1
                pass
            else:
                b=False
                break
    if b:
        result.append(i)
for i in result[-1]:
    print(i,end="")
print()
for i in result[0]:
    print(i,end="")
#print(result[0],result[-1])