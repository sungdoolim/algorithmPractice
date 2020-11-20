n=int(input())
#n=1
a=[]
for i in range(n):
    a.append(int(input()))
#a.append(10)
b=sorted(a,reverse=True)
result=[0]*(b[0]+1)
result[1]=1
result[2]=2
result[3]=4


def dp(i):
    if result[i]!=0:
        return 1

    for k in range(4,i+1):
        result[k]=result[k-1]+result[k-2]+result[k-3]

 

for i in a:

    dp(i)
    print(result[i])
    

    

    





