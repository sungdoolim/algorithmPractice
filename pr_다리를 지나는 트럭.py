from collections import deque
def solution(bridge_length, weight, truck_weights):
    stac=[0]*bridge_length
    q=deque(stac)
    trucks=deque(truck_weights)
    answer=0
    c=0
    while trucks:
        #print(q)
        answer+=1
        c-=q.popleft()
        #print(trucks[0])
        if c+trucks[0]<=weight:
            c+=trucks[0]
            q.append(trucks.popleft())
            
        else:
            q.append(0)


    #print(answer+bridge_length)
    return answer+bridge_length

solution(	100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10])