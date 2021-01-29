a,b=map(int,input().split())
ar=list(map(int,input().split()))
#print(ar)
i=0
j=1
count=0
while True:
    tmp=sum(ar[i:j])
    #print(i,j,tmp)
    if b==tmp:
        count+=1
        i+=1
        j+=1
    elif b<tmp:
        i+=1
    elif b>tmp:
        j+=1
    if i==j:
        j+=1
    if j==a+1:
        break
print(count)
