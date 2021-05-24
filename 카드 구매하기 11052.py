n=int(input())
ar=list(map(int,input().split()))
#print(ar)
result=[0]*(n)
#print(result)

result[0]=ar[0]

def dp():
    if n==1:
        print(result[0])
    else:
        result[1]=max(result[0]*2,ar[1])
        for i in range(1,n):
            for j in range(i):
                #print(result)
                result[i]=max(result[j]+result[i-j-1],result[i])
            result[i]=max(result[i],ar[i])
        #print(result)
        print(result[n-1])
dp()


