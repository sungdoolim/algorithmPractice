a,b=input().split()
ar=list(a)
br=list(b)
ar.reverse()
br.reverse()
la=len(ar)
lb=len(br)
result=[]
if la>lb:
    for i in range(lb):
        result.append(str(int(ar[i])+int(br[i])))
    for i in range(lb,la):
        result.append(ar[i])
else:
    for i in range(la):
        result.append(str(int(ar[i])+int(br[i])))
    for i in range(la,lb):
        result.append(br[i])
result.reverse()
for i in result:
    print(i,end="")