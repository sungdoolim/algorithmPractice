n=int(input())
ar=[]
for _ in range(n):
    ar.append(list(map(int,input().split())))
# for i in ar:
#     print(i)
count=0
result=[0,0,0]
def separate(s,a,b):
    boo=True
    global count
    init=ar[a][b]
    for i in range(a,a+s):
        for j in range(b,b+s):
            if ar[i][j]!=init:
                boo=False
                break
    if boo:
       # print(s,a,b)
        result[ar[a][b]+1]+=1
        
    else:
        for i in range(a,a+s,s//3):
            for j in range(b,b+s,s//3):
                separate(s//3,i,j)

separate(n,0,0)
#print(result)
for i in result:
    print(i)
