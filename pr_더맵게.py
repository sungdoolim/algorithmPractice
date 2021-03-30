import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    answer=0
    m=heapq.heappop(scoville)
    while m<K and scoville:
        answer+=1
        m2=heapq.heappop(scoville)
        heapq.heappush(scoville,m2*2+m)
        m=heapq.heappop(scoville)
    if m<K:
        return -1
    else:
        return answer
solution([1, 2, 3, 9, 10, 12], 7)