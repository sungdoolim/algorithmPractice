import sys
from itertools import permutations
r=sys.stdin.readline
n=int(r().rstrip())
number=['1','2','3','4','5','6','7','8','9']
num=list(permutations(number,3))
l=len(num)
#print(num)
# for i in num:
#     print(i)
ar=[]
strike=[]
ball=[]
result=[]
for _ in range(n):
    a,b,c=r().rstrip().split()
    ar.append(a)
    strike.append(b)
    ball.append(c)
#print(ar)
for i in range(l):
    #print(num[i])
    a,b,c=num[i][0],num[i][1],num[i][2]
    #print(a,b,c)
    for j in range(n):
        arv=ar[j]
       # print(arv,j)
        v1=arv[0]
        v2=arv[1]
        v3=arv[2]
        
        strv=strike[j]
        balv=ball[j]
        #s=0
        ba=0
        count=0
        if a==v1:
            count+=1           
        if b==v2:
            count+=1    
        if c==v3:
            count+=1
        if v1!=a and v1 in num[i]:
            ba+=1
        if v2!=b and v2 in num[i]:
            ba+=1
        if v3!=c and v3 in num[i]:
            ba+=1
        #print(a,b,c,v1,v2,v3,count,ba,strv,balv)
        if int(strv)==count and ba==int(balv) :
            if j==n-1:
                result.append(num[i])
        #    print("True")
        else:
            break

#print(result)
print(len(result))
            




