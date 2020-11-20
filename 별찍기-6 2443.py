n=int(input())

for i in range(n,0,-1):
    a=2*i-1
    for k in range(n-i):
        print(" ",end="")
    for j in range(a):

        print('*',end="")
    print()