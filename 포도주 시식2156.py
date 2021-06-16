n=int(input())
result=[0]*(n+1)
ar=[]
ckl=[0]*(n+1)
ckl[0]=0
ckl[1]=1
ar.append(0)
for _ in range(n):
    ar.append(int(input()))
#print(ar)
result[1]=ar[1]
if n==1:
    print(result[1])
elif n==2:
    result[2]=ar[1]+ar[2]
    print(result[2])
else:
    result[2]=ar[1]+ar[2]
    ckl[1]=1
    ckl[2]=1

    #print(result)
    for i in range(3,n+1):
     #   print(ckl)
        if ckl[i-1]==1 and ckl[i-2]==1:
            if result[i-1]> result[i-2]+ar[i]:
                result[i]=result[i-1]
            else:
                result[i]=result[i-2]+ar[i]
                ckl[i]=1
                ckl[i-1]=0
                
            if result[i-3]+ar[i-1]+ar[i]>result[i]:
                ckl[i-1]=1
                ckl[i]=1
                result[i]=result[i-3]+ar[i-1]+ar[i]

        else:
            result[i]=result[i-1]+ar[i]
            ckl[i]=1


    print(result[n])
    
