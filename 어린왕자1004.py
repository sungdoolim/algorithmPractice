tc=int(input())
for _ in range(tc):
    x1,y1,x2,y2=map(int,input().split())
    n=int(input())
    ar=[]
    result=[0]*n
    for _ in range(n):
        ar.append(list(map(int,input().split())))
    #print(ar)
    k=0
    for j in ar:
        a,b,r=j[0],j[1],j[2]
        if (x1-a)**2 + (y1-b)**2<r**2:
            result[k]=1
        k+=1
    k=0
    for j in ar:
        a,b,r=j[0],j[1],j[2]
        if (x2-a)**2 + (y2-b)**2<r**2:
            result[k]+=1
        k+=1
    #print(result)
    count=0
    for i in result:
        if i==1:
            count+=1
    print(count)