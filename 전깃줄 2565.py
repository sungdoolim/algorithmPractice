import sys
r=sys.stdin.readline
n=int(r().rstrip())
lis=[]
for _ in range(n):
    a,b=map(int,r().rstrip().split())
    lis.append([a,b])
result=[0]*(n+1)
result[0]=1
lis.sort()
for i in range(1,len(lis)):
   # print(result)
    for j in range(i):
        if lis[i][1]>lis[j][1]:
  #          print(lis[i][1],lis[j][1],end=",")
            result[i]=max(result[j],result[i])
    result[i]+=1
# print(result)
# print(lis)
print(n-max(result))
