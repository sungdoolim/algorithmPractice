n,m=map(int,input().split())
ar=[]
for _ in range(n):
    ar.append(int(input()))
end=max(ar)
start=0

while True:
  #  print(start,end)
    if start>end:
        print(end)
        break
    count=0
    mid=(start+end)//2
    mid=1 if mid==0 else mid
    for i in ar:
        count+=(i//mid)
    if count>=m:
        start=mid+1
    else:
        end=mid-1