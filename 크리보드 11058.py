n=int(input())
result=[0]*101
result[1]=1
result[2]=2
result[3]=3
result[4]=4
result[5]=5


def dp(i):
    result[i]=max(result[i-1]+1,result[i-3]*2,result[i-4]*3,result[i-5]*4)
for i in range(6,n+1):
    dp(i)
#print(result)
print(result[n])
