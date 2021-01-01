n,m=map(int,input().split())
ar=[]
for _ in range(n):
    ar.append(input())
br=[]
for _ in range(n):
    br.append(input())

#print(ar,br)
result=[]
for i in range(n):
    tmp=ar[i]
    l=len(tmp)
    newstr=""
    for j in range(l):
        newstr+=tmp[j]*2
    
    result.append(newstr)
resultbool=False
for j in range(n):
    if result[j]==br[j]:
        
        resultbool=True
    else:
        resultbool=False
        break
if resultbool:
    print("Eyfa")
else:
    print("Not Eyfa")