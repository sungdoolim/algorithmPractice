n=int(input())
ar=[]
for _ in range(n):
    ar.append(list(input()))

# for i in ar:
#     print(i)
result=""
def split_con(a,b,s):
    global result
    boo=True
    init=ar[a][b]
    for i in range(a,a+s):
        for j in range(b,b+s):
            if ar[i][j]!=init:
                
                boo=False
                break
    if boo:
        #print(ar[a][b])
        result+=ar[a][b]
    else:
        result+="("
        for i in range(a,a+s,s//2):
            for j in range(b,b+s,s//2):
                split_con(i,j,s//2)
        result+=")"
split_con(0,0,n)
print(result)