import sys
a,b=map(int,sys.stdin.readline().rstrip().split())
ar=list(map(int,sys.stdin.readline().rstrip().split()))
point1=0
point2=1
result=100000
while True:
    if point2>a:
        break;
    if point2-point1>=result:
        point1+=1
    if sum(ar[point1:point2])>=b:
        result=point2-point1
        point1+=1
        if point1==point2:
            point2+=1
    else:
        point2+=1

if result==100000:
    print(0)
else :
    print(result)

