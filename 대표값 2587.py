n=int(input())
#n=5

ar=list(map(int,input().split()))
stu=[i for i in range(1,n+1)]
#print(ar,stu)
result=[0]*(n+1)

for i in range(1,n):
    k=i-ar[i]#k인덱스에 들어갈것.
    tmp=stu[i]
    stu[k+1:i+1]=stu[k:i]
    stu[k]=tmp
for i in stu:
    print(i,end=" ")

