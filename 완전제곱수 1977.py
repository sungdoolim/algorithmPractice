import math
n=int(input())
m=int(input())
tmpn=int(math.sqrt(n))
tmpm=int(math.sqrt(m))
#print(tmpn,tmpm)
result=[]
if tmpn**2==n:
    result.append(n)
for i in range(tmpn+1,tmpm):
    result.append(i**2)
if n<tmpm**2<=m and n!=m:
    result.append(tmpm**2)

if result:
    # for i in result:
    #     print(i, end=" ")
    #print()
    print(sum(result))   
    print(result[0])
    
else:
    print(-1)
