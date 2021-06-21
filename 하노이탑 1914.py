n=int(input())
result=[]
count=0
hanoiResult=[0]*(n+1)
def hanoi(i,start,mid,end):
    global count
    count+=1
    if i==1:
        result.append([start,end])
    else:
        hanoi(i-1,start,end,mid)
        result.append([start,end])
        hanoi(i-1,mid,start,end)



if n>20:
   
    print(2**n-1)

else:    
    hanoi(n,1,2,3)
    print(count)
    for i in result:
        print(i[0],i[1])

