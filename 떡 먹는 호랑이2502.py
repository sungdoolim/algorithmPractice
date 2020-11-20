import sys
a,b=map(int,sys.stdin.readline().rstrip().split())
#print(a,b)

result=[0]*a
result[a-1]=b
tmp=[0]*31
tmp[1]=1
tmp[2]=0
for i in range(3,31):
    tmp[i]=tmp[i-1]+tmp[i-2]
#print(tmp)

oneday=tmp[a]
twoday=tmp[a+1]
#print(oneday,twoday)
counta=1
countb=0
b-=oneday
while True:
    if b==0:
        break;
    elif b%twoday==0:
        countb=int(b/twoday)
        break
    else:
        b-=oneday
        counta+=1
print(counta)
print(countb)
