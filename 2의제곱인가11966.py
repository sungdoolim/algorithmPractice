n=int(input())
def isbinary():
    for i in range(1,31):
        if n==2**i:
            print(1)
            return
    print(0)
if n==1:
    print(1)
else:
    isbinary()