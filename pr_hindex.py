def solution(citations):
    m=0
    M=max(citations)    
    while True:
        if m>M:
            break
        count=0
        mid=(m+M)//2
        for i in citations:
            if i>=mid:
                count+=1
        if count>=mid:
            m=mid+1
        else:
            M=mid-1
    print(M)
    return M


solution([22, 42]  )