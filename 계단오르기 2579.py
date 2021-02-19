n=int(input())
ar=[]
for _ in range(n):
    ar.append(int(input()))
#print(ar)
result=[0]*n
ckl=[0]*n
result[0]=ar[0]
ckl[0]=0
if n==1:
    print(sum(ar))
elif n==2:
    print(sum(ar))
elif n==3:
    print(max(ar[0]+ar[2],ar[1]+ar[2]))
else:
    result[1]=ar[1]+ar[0]
    ckl[1]=1
    a=0
    b=0
    for i in range(n):

        a=result[i-2]
        if ckl[i-1]:
            b=result[i-3]+ar[i-1]
        else:
            b=result[i-1]
        
        if a>=b:
            result[i]=result[i-2]+ar[i]
        else:
            result[i]=b+ar[i]
            ckl[i]=1

    print(result[-1])

