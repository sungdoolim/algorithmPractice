n,m=map(int,input().split())
start=0
k=0
b=False
for i in range(m-1,100):
    start=(2*n-i**2-i)/(2*(1+i))
    if start==int(start) and start>=0:
        #print(start,i)
        k=i+1
        b=True
        break
if b :
    start=int(start)
    for i in range(k):
        print(start+i,end=" ")
else:
    print(-1)
    #print(start)
