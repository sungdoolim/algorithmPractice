from itertools import permutations
def solution(numbers):
    areto=[0]*10000000
    areto[0]=1
    areto[1]=1
    for i in range(2,10000000):
        if areto[i]==0:
            j=2
            while i*j<10000000:
                areto[i*j]=1
                j+=1




    count=0
    ar=list(numbers)
    al=len(ar)
    for i in range(1,al+1):
        pr=list(permutations(ar,i))
        pr=set(pr)
        print(pr)
        for j in pr:
            s=""
            for k in j:
                s+=k
            #print(s)
            if areto[int(s)]==0:
                areto[int(s)]=1
                print(int(s))
                count+=1
            



    return count

solution("011")