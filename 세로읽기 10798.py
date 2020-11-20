import sys
ar=[]
for _ in range(5):
    ar.append(sys.stdin.readline().rstrip())
print(ar)
for i in range (15):
    for k in range(5):
        if len(ar[k])>i:
            print(ar[k][i],end="")

