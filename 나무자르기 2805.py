n,m=map(int,input().split())
ar=list(map(int,input().split()))
#print(ar)
end=max(ar)
start=0
while start<=end:
    #print(start,end)
    mid=(start+end)//2
    obj=0
    for i in ar:
        k=(i-mid)
        if k>0:
            obj+=k
    if obj>=m:
        start=mid+1
    else:
        end=mid-1
print(end)