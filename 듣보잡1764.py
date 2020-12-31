n,m=map(int,input().split())
ar=[]
br=[]
for _ in range(n):
    ar.append(input())
for _ in range(m):
    br.append(input())

#print(ar,br)
arset=set(ar)
brset=set(br)
result=sorted(list(arset&brset))



print(len(result))
for i in result:
    print(i)