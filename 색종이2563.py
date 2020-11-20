import sys
n=int(input())
ar=[]
for _ in range(n):
    ar.append(list(map(int,sys.stdin.readline().rstrip().split())))
print(ar)
result=[[0]*101 for _ in range(101)]
#print(result)

for i in ar:
    for j in range(i[0],i[0]+10):
        for k in range(i[1],i[1]+10):
            result[j][k]=1

sum=0
for i in range(101):
    for j in range(101):
        if result[i][j]:
            sum+=1
print(sum)
