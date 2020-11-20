n=int(input())
result=[0]*(n+1)
result[0]=0
result[1]=1

def dp(n):
    result[n]=result[n-1]+result[n-2]

for i in range(2,n+1):
    dp(i)
    #print(result)
    

print(result[n])
