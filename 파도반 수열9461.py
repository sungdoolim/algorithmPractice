n=int(input())
ar=[]
for _ in range(n):
    ar.append(int(input()))
pado=[0]*101
pado[0]=0
pado[1]=1
pado[2]=1
# 1, 1, 1, 2, 2, 3, 4, 5, 7, 9
pado[3]=1
pado[4]=2
pado[5]=2
pado[6]=3
pado[7]=4
pado[8]=5
pado[9]=7
pado[10]=9
for i in range(11,101):
    pado[i]=pado[i-1]+pado[i-5]

for i in ar:
    print(pado[i])

