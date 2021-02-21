n,m=map(int,input().split())
ar=[n]
while True:
    a=ar[-1]
    br=list(str(a))
    bl=len(br)
    s=0
    for i in range(bl):
        s+=int(br[i])**m
    if s not in ar:
        ar.append(s)
    else:
        ar=ar[:ar.index(s)]
        break
print(len(ar))
