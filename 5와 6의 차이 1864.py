a,b=input().split()
al=len(a)
bl=len(b)
newa=""
Newa=""
newb=""
Newb=""
for i in range(al):
    if a[i]=='5' or a[i]=='6':
        newa+='5'
        Newa+='6'
    else:
        newa+=a[i]
        Newa+=a[i]
for i in range(al):
    if b[i]=='5' or b[i]=='6':
        newb+='5'
        Newb+='6'
    else:
        newb+=b[i]
        Newb+=b[i]
print(int(newa)+int(newb),end=" ")
print(int(Newa)+int(Newb))

