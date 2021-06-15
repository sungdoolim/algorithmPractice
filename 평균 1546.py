n=int(input())
ar=[]

ar=list(map(int,input().split()))
#print(ar)
M=max(ar)
br=[]
sum=0
while ar:
    k=ar.pop()
    sum+=k/M*100
print(sum/n)