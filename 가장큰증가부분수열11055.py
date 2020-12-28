n=int(input())
ar=list(map(int,input().split()))
#print(ar)
result=ar.copy()
#print(result)

for i in range(n):
    r=ar[i]
    for j in range(i+1):
        if ar[j]<ar[i]:
            r=max(r,result[j]+ar[i])
    result[i]=r
#print(result)

print(max(result))