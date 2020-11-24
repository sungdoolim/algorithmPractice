from math import sqrt
from bisect import bisect_left
import sys
maximum=1000001
sosu=[]


wrong="Goldbach's conjecture is wrong."


def areto():
    prime = [1] * maximum
    prime[0]=0
    prime[1]=0
    for idx in range(2, maximum): 
        if prime[idx]: 
            sosu.append(idx)
            jmp = 2 
            while idx*jmp < maximum: 
                prime[idx*jmp] = 0 
                jmp += 1
areto()
sosu.pop(0)
#print(sosu)


n=int(sys.stdin.readline().rstrip())
while n!=0:
    start=0
    end=bisect_left(sosu,n)-1
    while True:
        if start>end:
            print(wrong)
            break;
        elif sosu[start]+sosu[end]<n:
            start+=1
    
        elif sosu[start]+sosu[end]>n:
            end-=1

        else:
            print(str(n)+" = "+str(sosu[start])+" + "+str(sosu[end]))
            break;



    n=int(sys.stdin.readline().rstrip())