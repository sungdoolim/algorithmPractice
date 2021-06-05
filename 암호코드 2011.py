ar=list(input())
#print(ar)
l=len(ar)
result=[0]*(l+2)
result[0]=1
if l==1:
    if ar[0]=='0':
        print(0)
    else:
        print(1)
elif l==2:
    if ar[1]=='0':
        if ar[0]=='0' or ar[0]>'2':
            print(0)
        else:
            print(1)
    elif ar[0]+ar[1]<'27':
        print(2)
    else:
        print(1)
else:
    if ar[0]=='0':
        
        l=2
    
    elif ar[1]=='0':
        if ar[0]>'2':
            
            l=2
        else:
            result[1]=1
    elif ar[0]+ar[1]<'27':
        result[1]=2
        result[0]=1
    else:
        result[1]=1
        

    for i in range(2,l):
        if ar[i]=='0':
            if ar[i-1]=='0' or ar[i-1]>'2':
                
                break
            result[i]=result[i-2]%1000000
        elif ar[i-1]=='0':
            result[i]=result[i-1]%1000000
        elif ar[i-1]+ar[i]<'27':
            result[i]=(result[i-1]+result[i-2])%1000000
        else:
            result[i]=result[i-1]%1000000




    #print(result)
    print(result[l-1])

