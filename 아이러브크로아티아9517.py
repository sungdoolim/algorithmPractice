start=int(input())
n=int(input())
m=210
ar=[]

for _ in range(n):
    a,b=input().split()
    ar.append((int(a),b))
#print(ar)

for i,j in ar:
    m-=i
    if m<0:
        print(start)
        break;
    elif m>=0 and j=='T':
        start+=1
        if start==9:
            start=1



    