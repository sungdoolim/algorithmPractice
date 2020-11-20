import sys
n=int(sys.stdin.readline().rstrip())
ar=[]
for i in range(n):
    ar.append(list(map(int,sys.stdin.readline().rstrip().split())))
#print(n,ar)
result=[[10000]*3 for _ in range(n)]
result[0]=ar[0]
#print(result)
def dp():
    for i in range(1,n):
        for j in range(3):
            if j==0:
                a= result[i-1][1] if result[i-1][2]>result[i-1][1] else result[i-1][2]
                result[i][j]=a+ar[i][j]
            elif j==1:
                a= result[i-1][2] if result[i-1][0]>result[i-1][2] else result[i-1][0]
                result[i][j]=a+ar[i][j]
            else:
                a= result[i-1][0] if result[i-1][1]>result[i-1][0] else result[i-1][1]
                result[i][j]=a+ar[i][j]


if n==1:
    print(min(result[0]))
else:
    dp()
    print(min(result[n-1]))
