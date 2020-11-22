from math import gcd
n,m=map(int,input().split())
print(gcd(n,m))#공약수
i=1
while True:
    k=m*i
    if (k%n)==0:
        print(k)
        break;
    else:i+=1
