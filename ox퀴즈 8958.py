import sys
n=int(sys.stdin.readline().rstrip())

ar=[]
for _ in range(n):
    ar.append(sys.stdin.readline().rstrip())
result=[]
#print(ar)
for i in range(n):
    k=len(ar[i])
    tmp=[]
    count=0
    for j in range(k):
        if ar[i][j]=='O':
            count+=1
            tmp.append(count)
        else:
            count=0
    result.append(tmp)
    #print(result)

for i in result:
    sum=0
    for j in i:
        sum+=j
    print(sum)
    

