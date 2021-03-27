from math import ceil
def solution(progresses, speeds):
    l=[]
    for a,b in zip(progresses,speeds):
        d=ceil((100-a)/b)
        l.append(d)

    print(l)
    tmpl=l.pop(0)
    count=1
    result=[]
    while l:
        ttmpl=l.pop(0)
        if tmpl>=ttmpl:
            count+=1
        else:
            result.append(count)
            count=1
            tmpl=ttmpl
    result.append(count)

    print(result)

    
    return result
arr=[93, 30, 55]
brr= [1, 30, 5]
ar=	[95, 90, 99, 99, 80, 99]
br=[1, 1, 1, 1, 1, 1]
solution([99, 1, 99, 1], [1, 1, 1, 1])