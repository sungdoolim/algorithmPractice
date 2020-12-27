n=int(input())
ar=list(map(int,input().split()))
#print(ar)
bil=[1]*n
bir=[0]*n
for i in range(n):
    r=1
    for j in range(i+1):
        if ar[j]<ar[i]:
            r=max(r,bil[j]+1)
    bil[i]=r
    r=1

for i in range(n-1,-1,-1):
    r=1
    for j in range(n-1,i,-1):
        if ar[j]<ar[i]:
            r=max(r,bir[j]+1)
    bir[i]=r
    
# print(bil)
# print(bir)
result=[0]*n
for i in range(n):
    result[i]=bil[i]+bir[i]

print(max(result)-1)

