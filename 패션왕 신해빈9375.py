tn=int(input())
for _ in range(tn):
    n=int(input())
    ar={}
    for _ in range(n):
        s=input().split()
        if s[1] in ar:
            ar[s[1]]+=1
        else:
            ar[s[1]]=1
    #print(ar)
    s=1
    for i in ar.values():
        s*=(i+1)
    print(s-1)
