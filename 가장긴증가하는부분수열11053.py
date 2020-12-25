n=int(input())
ar=list(map(int,input().split()))
#print(ar)
result=[1]*n

for i in range(n):
    r=1
    for j in range(i+1):
        if ar[j]<ar[i]:
            r=max(r,result[j]+1)
    result[i]=r
#print(result)
print(max(result))