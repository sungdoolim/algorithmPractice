from itertools import permutations
import math
def solution(expression):
    ar=["+","*","-"]
    ar=list(permutations(ar,3))
    # print(ar)
    result=[]
    for permu in ar:
        a,b,c=permu
        # print(a,b,c)
        tree1=expression.split(c)
        r=[]
        for node1 in tree1:
            
            endnode=node1.split(b)
            e=[]
            for k in endnode:
                e.append(str(eval(k)))
            # print("new:",e)
            newstr=""
            for i in e:
                newstr+=(i+b)
            newstr=newstr[:len(newstr)-1]
            # print("str:",newstr)
            r.append(str(eval(newstr)))
        # print(r)
        newstr=""
        for i in r:
            newstr+=(i+c)
        newstr=newstr[:len(newstr)-1]
        result.append(abs(eval(newstr)))
    # print(result)
    # print(max(result))
        
    answer = 0
    return max(result)



solution("100-200*300-500+20")