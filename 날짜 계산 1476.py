e,s,m=1,1,1
count=1
E,S,M=map(int,input().split())
# print(e,s,m)
# print(E,S,M)
while True:
    if e==E and s==S and m==M:
        print(count)
        break;
    count+=1
    e+=1
    if e==16:
        e=1
    s+=1
    if s==29:
        s=1
    m+=1
    if m==20:
        m=1


