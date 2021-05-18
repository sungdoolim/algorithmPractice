n=int(input())
ar=[]
for _ in range(n):
    ar.append(list(map(int,input().split())))
ar.sort(key=lambda x:(x[1],x[0]))
for i in ar:
    print(i[0],i[1])