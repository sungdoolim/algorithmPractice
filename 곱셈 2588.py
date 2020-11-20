a=int(input())
b=list(map(int,input()))
result=[]

for i in b:
    result.append(a*i)
l=len(result)
for i in range(l):
    print(result[l-i-1])
print(result[0]*(100)+result[1]*10+result[2])
