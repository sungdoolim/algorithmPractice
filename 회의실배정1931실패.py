#회의실 배정 1931


n=int(input())
#n=11
b=[]

for i in range(n):
    a=list((map(int,input().split())))
    b.append(a)

b=sorted(b,key=lambda x:x[1]-x[0])
print(b)
result=[0]*(2^31-1)
count=0
for i in range(n):
    ar=b[i][0]
    br=b[i][1]
    if 1 in result[ar:br+1]:
        continue;
    if result[ar]==0 or result[ar]==2:
        result[ar]=2
    else:
        continue;
    
    if result[br]==0 or result[br]==2:
        result[br]=2
    else:
        continue;
    for j in range(ar+1,br):
        result[j]=1
    count+=1
#    print(result)
print(count)


