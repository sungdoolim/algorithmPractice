a,b,v=map(int,input().split())
count=1
tmp=a-b
i=2
k=int(v/(a-b))
tt=(a-b)*(k-1)
count=k-1
tt+=b
while True:
    if tt>=v:
        while True:
            tt=tt-a+b
            if tt<v:
                break
            else:
                count-=1
        break;
    else:
        tt=tt-b+a
        count+=1
print(count)
