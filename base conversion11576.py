future,now=map(int,input().split())
l=int(input())
ar=list(map(int,input().split()))
al=len(ar)
count=0
r=0
for i in range(al-1,-1,-1):
    r+=ar[i]*(future**count)
    count+=1
result=[]
while r!=0:
    result.append(r%now)
    r//=now

for i in range(len(result)-1,-1,-1):
    print(result[i],end=" ")
