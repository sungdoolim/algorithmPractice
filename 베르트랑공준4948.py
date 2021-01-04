import math
m=123456*2
aretos=[0]*(m+1)
aretos[0]=1
aretos[1]=1

M=int(math.sqrt(m))+1
for i in range(2,M):
    if aretos[i]==0:
        
        j=2
        while True:
            tmp=i*j
            if tmp>m:
                break;
            else:
                aretos[i*j]=1
                j+=1

#print(aretos)
ar=[]
a=int(input())
while a!=0:
    ar.append(a)
    a=int(input())
#print(ar)
for i in ar:
    count=0
    for j in range(i+1,2*i+1):
        if aretos[j]==0:
            count+=1
    print(count)