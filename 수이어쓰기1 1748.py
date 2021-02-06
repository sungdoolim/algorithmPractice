n=input()
ln=len(n)
nn=int(n)
s=0
i=1
if nn<10:
    s=nn
    print(s)
else:
    s+=9
    for i in range(1,ln-1):
        s+=(i+1)*(10**(i+1)-10**(i))
    s+=ln*(nn-10**(ln-1)+1)
    print(s)


