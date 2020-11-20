a=int(input())
fac=1
for i in range(2,a+1):
    fac*=i
#print(fac)
refac=str(fac)
#print(refac)
l=len(refac)
l-=1
count=0
for i in range(l,-1,-1):
    if refac[i]=='0':
        count+=1
    else:
        break;
print(count)