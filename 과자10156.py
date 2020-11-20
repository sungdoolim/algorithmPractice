import sys

a,b,c=map(int,sys.stdin.readline().split())
k=a*b-c
if k>=0:
    print(k)
else:
    print(0)
