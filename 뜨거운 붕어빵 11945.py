a,b=map(int,input().split())
ar=[]
for _ in range(a):
    ar.append(list(map(int,input())))
#print(ar)
for i in ar:
    for j in range(b-1,-1,-1):
        print(i[j],end="")
    print()