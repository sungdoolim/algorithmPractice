import sys
n=int(sys.stdin.readline().rstrip())
ar=[]
for _ in range(n):
    a,b=map(int,sys.stdin.readline().rstrip().split())
    if a>=10:
        a%=10
        #print(a)
    if a==1 or a==5 or a==6 :
        ar.append(a)
    elif a==0:
        ar.append(10)
    elif a==2:
        if b%4==0:
            ar.append(6)
        elif b%4==1:
            ar.append(2)
        elif b%4==2:
            ar.append(4)
        elif b%4==3:
            ar.append(8)
    elif a==3:
        if b%4==0:
            ar.append(1)
        elif b%4==1:
            ar.append(3)
        elif b%4==2:
            ar.append(9)
        elif b%4==3:
            ar.append(7)
    elif a==4:
        if b%2==0:
            ar.append(6)
        elif b%2==1:
            ar.append(4)
    elif a==7:
        if b%4==0:
            ar.append(1)
        elif b%4==1:
            ar.append(7)
        elif b%4==2:
            ar.append(9)
        elif b%4==3:
            ar.append(3)
    elif a==8:
        if b%4==0:
            ar.append(6)
        elif b%4==1:
            ar.append(8)
        elif b%4==2:
            ar.append(4)
        elif b%4==3:
            ar.append(2)
    elif a==9:
        if b%2==0:
            ar.append(1)
        elif b%2==1:
            ar.append(9)



for i in ar:
    print(i)