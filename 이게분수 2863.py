a,b=map(int,input().split())
c,d=map(int,input().split())
M=a/c+b/d
m2=c/d+a/b
m3=d/b+c/a
m4=b/a+d/c
index=0
# pass는 다 지워도 되겠지!
if M>=m2:
    pass
else:
    M=m2
    index=1
if M>=m3:
    pass
else:
    M=m3
    index=2
if M>=m4:
    pass
else:
    M=m4
    index=3
    
print(index)
