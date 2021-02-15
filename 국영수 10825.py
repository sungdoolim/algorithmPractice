import sys

n=int(sys.stdin.readline().rstrip())
ar=[]
for _ in range(n):
    a,b,c,d=sys.stdin.readline().rstrip().split()
    ar.append([a,int(b),int(c),int(d)])
ar.sort(key=lambda x:(-x[1],x[2],-x[3],x[0]))
for i in ar:
    print(i[0])