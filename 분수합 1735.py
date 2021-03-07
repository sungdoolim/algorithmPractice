from math import gcd
def lcm(a, b):
    return a * b // gcd(a, b)

a,b=map(int,input().split())
c,d=map(int,input().split())
mother=int(lcm(b,d))
a*=(mother//b)
c*=(mother//d)
son=int(a+c)
while True:
    isgcd=int(gcd(son,mother))
    if isgcd==1:
        break
    mother//=isgcd
    son//=isgcd

print(son,mother)