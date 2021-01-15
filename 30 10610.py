n=list(map(int,list(input())))

n.sort(reverse=True)

if n[-1]==0 and sum(n)%3==0:
    newstr=""
    for i in n:
        newstr+=str(i)
    print(newstr)
    
else:
    print(-1)