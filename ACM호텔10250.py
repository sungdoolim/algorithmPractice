n=int(input())
ar=[]
for _ in range(n):
    a,b,c=map(int,input().split())
    k=0
    kk=c%a
    if kk==0:
        kk=a*100
        k=int(c/a)
    else:
        kk*=100
        k=int(c/a)+1
    
        
    ar.append(kk+k)
for i in ar:
    print(int(i))