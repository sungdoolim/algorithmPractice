import sys
r=sys.stdin.readline
ar=list(r().rstrip())
n=int(r().rstrip())
cursor=len(ar)
arl=cursor
br=[]
#print(ar)
#print(br)

for _ in range(n):
    a=list(r().rstrip().split())
    if a[0]=="L" :
        if ar!=[]:
            br.append(ar.pop())
    elif a[0]=="D" :
        if br!=[]:
            ar.append(br.pop())
    elif a[0]=="B" :
        if ar!=[]:
            ar.pop()
    else:
        ar.append(a[1])
    #print(ar,br)

for i in ar:
    print(i,end="")
br.reverse()
for j in br:
    print(j,end="")
