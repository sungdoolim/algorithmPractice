a,b=map(int,input().split())
ar=list(map(int,input().split()))
br=list(map(int,input().split()))
result=ar+br
result.sort()
for i in result :
    print(i,end=" ")