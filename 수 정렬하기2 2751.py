import sys
# sys.stdin.readline().rstrip()
n=int(sys.stdin.readline().rstrip())
ar=[]
for _ in range(n):
    ar.append(int(sys.stdin.readline().rstrip()))
ar.sort()
for i in ar:
    print(i)