from collections import deque
def solution(priorities, location):

    sorting=sorted(priorities)
    print(sorting)
    l=len(priorities)
    pq=deque(priorities)
    r=[i for i in range(l)]
    rq=deque(r)
    count=0
    m=sorting.pop()
    while True:
        
        print(pq)
        print(rq)
        print(count)
        k=pq.popleft()
        index=rq.popleft()
        if k==m:
            count+=1
            if index==location:
                print(count)
                return count
        
            m=sorting.pop()
            
        else:
            pq.append(k)
            rq.append(index)

    print(r)


    answer = 0
    return answer

solution(	[1, 1, 9, 1, 1, 1], 0)