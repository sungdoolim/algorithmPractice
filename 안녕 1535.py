import sys

n=int(sys.stdin.readline().rstrip())
hp=list(map(int,sys.stdin.readline().rstrip().split()))
happy=list(map(int,sys.stdin.readline().rstrip().split()))
hphappy=list(zip(hp,happy))
#print(hphappy)
m=-1
def bruteForce(i,hpv,happyv):
    hpv+=hp[i]
    #print(i)
    global m
    if hpv>=100:
        m=max(m,happyv)
    else:
        happyv+=happy[i]
        if i+1==n:
            m=max(m,happyv)

        else:
            for j in range(i+1,n):
                bruteForce(j,hpv,happyv)
        
        


for i in range(n):
    bruteForce(i,0,0)
print(m)