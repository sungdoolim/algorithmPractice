def solution(number, k):
    
    num=list(map(int,list(number)))
    num.reverse()
    count=0
    result=[]
    while num:
        a=num[-1]
        print(a,result)
        if result :
            if result[-1]<a:
                result.pop()
                count+=1
                if count==k:
                    while num:
                        result.append(num.pop())
                    break
            else:
                result.append(num.pop())
        else:
            result.append(num.pop())
    while count!=k:
        result.pop()
        count+=1
    s=""
    for i in result:
        s+=str(i)
    print(s)

    return s
solution(	"4177252841", 4)