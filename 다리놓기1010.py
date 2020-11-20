case=int(input())
caselist=[]
for _ in range(case):
    caselist.append(list(map(int,input().split())))
#print(caselist)
result=[0]*case
for i in range(case):
    n=caselist[i][0]
    m=caselist[i][1]
    div1=1
    div2=1
    for j in range(m,n,-1):
        div1*=j
    for k in range(m-n,1,-1):
        div2*=k
    result[i]=int(div1/div2)

for i in result:
    print(i)
