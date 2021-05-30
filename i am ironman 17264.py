n,m=map(int,input().split())
plus,minus,bronz=map(int,input().split())

a={}
for _ in range(m):
    c,d=input().split()
    a[c]=d

#print(a)

ar=a.keys()
hap=0
b=True
for _ in range(n):
    #print(hap)
    s=input()
    if not b:
        continue
    if s in ar:
        if a[s]=="W":
            hap+=plus
            if hap>=bronz:
                
                b=False
                
        else:
            hap-=minus
            if hap<0:
                hap=0
    else:
        hap-=minus
        if hap<0:
            hap=0
if b:
    print("I AM IRONMAN!!")
else:
    print("I AM NOT IRONMAN!!")

    
