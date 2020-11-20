n=int(input())
ar=[]
for _ in range(n):
    ar.append(int(input()))
result0=[1000]*41
result1=[1000]*41

result0[0]=1
result1[0]=0
result0[1]=0
result1[1]=1
def df(i):
    result0[i]=result0[i-1]+result0[i-2]
    result1[i]=result1[i-1]+result1[i-2]

for i in range(2,41):
    df(i)



for i in ar:
    print(result0[i],result1[i])
        
