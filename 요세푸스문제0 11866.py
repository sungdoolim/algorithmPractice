n,k=map(int,input().split())
ar=[i for i in range(1,n+1)]
#print(ar)
tmp=k-1
result=[]
result.append(ar.pop(tmp))
while ar:
    tmp+=(k-1)
    while tmp>=len(ar):
        tmp-=len(ar)
    result.append(ar.pop(tmp))

#print(result)
print("<",end="")
for i in range(len(result)):
    if i==len(result)-1:
        print(result[i],end="")
    else:
        print(result[i],end=", ")
print(">")
