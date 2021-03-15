import sys

n=int(sys.stdin.readline().rstrip())
ar=list(map(int,sys.stdin.readline().rstrip().split()))
m=int(sys.stdin.readline().rstrip())
start=0
end=m
mid=0
if sum(ar)<=m:
    print(max(ar))
else:
    while True:
        #print(start,end)
        mid=(start+end)//2
        if start>end: # 부등호가 있느냐에 따라 답이 달라진다...
            break
        hap=0
        #print(start,mid,end)
        
        for i in ar:
            if i<=mid:
                hap+=i
            else:
                hap+=mid

        if hap>m:
            end=mid-1
        else:
            start=mid+1
            
    print(mid)
