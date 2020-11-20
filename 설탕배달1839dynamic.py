#설탕배달
#다이나믹인가??
def dynam(i):
    #print(i,end="")
    global result
    result[i]=min(result[i-3],result[i-5])+1
    
    

n= int(input())
if n<3 or n==4:
    print(-1)

elif n==3 or n==5:
    print(1)

else:
    global result  
    result=[10001]*(n+1)
    result[3]=1

    result[5]=1
    for i in range(6,n+1):
        dynam(i)
    #print(result)
    if(result[n]<1001):
        print(result[n])
    else:
       print(-1)
