n=int(input())
ar=list(map(int,input().split()))
br=list(map(int,input().split()))
sum=0
al=len(ar)
m=br[0]
for i in range(al):
    #print(ar[i]*min(br[:i+1]))
    m=min(m,br[i])
    sum+=(ar[i]*m)
print(sum)