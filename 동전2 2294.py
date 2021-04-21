n,k=map(int,input().split())
ar=[]
result=[0]*(k+1)
for _ in range(n):
    t=int(input())
    if t>k:
        continue
    ar.append(t)
    result[t]=1
ar.sort()
#print(result)
if not ar:
    print(-1)
else:
    for i in range(ar[0]+1,k+1):
        #print(result,i)
        if result[i]!=0:
            continue
        m=100000
        for j in ar:
        # print(m, end =" ")
            if i-j<0 or result[i-j]==0:
                continue
            else:
                m=min(m,result[i-j])

        if m==100000:
            continue
        else:
            result[i]=m+1
    #print(result)
    if result[k]==0:
        print(-1)
    else:
        print(result[k])