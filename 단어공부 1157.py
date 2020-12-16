ar=input()
l=len(ar)
alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
result=[0]*26
for i in range(l):
    k=ord(ar[i])
    if k>96:
        result[k-97]+=1
    elif k<97:
        result[k-65]+=1
#print(result)
m=max(result)
v=result.index(m)
result[v]-=1
if m in result:
    print("?")
else:
    print(alphabet[v])

