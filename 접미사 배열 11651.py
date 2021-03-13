n=input()
result=[]
nl=len(n)
for i in range(nl):
    result.append(n[i:])
result.sort()
for i in result:
    print(i)