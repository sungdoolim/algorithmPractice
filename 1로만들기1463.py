n=int(input())
ar=[0]*(n+5)
ar[1]=0
ar[2]=1
ar[3]=1

for i in range(4,n+1):
    m2=10000000
    m3=10000000
    if i%2==0:
        m2=ar[i//2]
    if i%3==0:
        m3=ar[i//3]
    ar[i]=min(ar[i-1]+1,m2+1,m3+1)
print(ar[n])