import sys

n=int(sys.stdin.readline().rstrip())
ar=[]
ar.append(0)
ar+=list(map(int,sys.stdin.readline().rstrip().split()))
#print(ar)
result=[1]*(n+1)
result[1]=1
for i in range(2,n+1):
    for j in range(1,i):
        if ar[j]<ar[i]:
            result[i]=max(result[i],result[j]+1)
    
#print(result)
print(max(result))