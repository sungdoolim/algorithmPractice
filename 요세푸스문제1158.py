n,m=map(int,input().split())
m-=1
nn=n
br=[i for i in range(1,n+1)]
#print(br)
ar=[]
i=0
while br:
    i+=m
    #print(br,i,n)
    while i>=n:
        i-=n
        #print(i)
    ar.append(br.pop(i))
    n-=1
#print(ar)
print('<',end="")
for l in range(nn):
    if l!=nn-1:
        print(str(ar[l])+",",end=" ")
    else:
        print(str(ar[l])+">")
