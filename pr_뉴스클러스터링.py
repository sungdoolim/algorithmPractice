def solution(str1, str2):
    answer = 0
    str1=str1.upper()
    str2=str2.upper()
    sl=len(str1)
    sl2=len(str2)
    ar1=[]
    ar2=[]
    l1=0
    l2=0
    for i in range(sl-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            ar1.append(str1[i:i+2])
            l1+=1
    for i in range(sl2-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            ar2.append(str2[i:i+2])
            l2+=1
    count=0
    for i in ar1:
        if i in ar2:
            ar2.remove(i)
            count+=1
    if l1+l2==count:
        return (65536)
    else:
        return (int((count/(l1+l2-count))*65536))

        
        
    # print(ar1)
    # print(ar2)
    #return answer


solution("FRANCE", "french")