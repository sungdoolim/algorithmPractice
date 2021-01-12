n=int(input())
ar=[i for i in range(1,n+1)]
#print(ar)

one=0
two=1
count=0
while one!=n-1:
    tmp=sum(ar[one:two])
    if tmp==n:
        #print(one,two)
        count+=1
        one+1
        two+=1
    elif tmp>n:
        one+=1
    else:
        two+=1


    #print(tmp)
print(count+1)