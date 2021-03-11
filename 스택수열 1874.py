n=int(input())
ar=[0]*n
for i in range(n):
    ar[i]=int(input())
#print(ar)
stac=[]
result=[]
i=1
j=1
while True:
    #print(stac)
    if i>n or j>n+1:
        break
    if stac and stac[-1]==ar[i-1]:
        stac.pop()
        result.append('-')
        i+=1
    else:
        stac.append(j)
        j+=1
        result.append('+')
if stac:
    print("NO")
else:
    for i in result:
        print(i)




