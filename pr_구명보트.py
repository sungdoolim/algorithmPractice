from collections import deque
def solution(people, limit):
    count=0
    people.sort(reverse=True)
    people=deque(people)
    pl=len(people)
    while people:
        print(people,"?")
        
        if pl>1 and people[0]+people[-1]<=limit:
            people.pop()
            people.popleft()
            pl-=2
        else:
            people.popleft()
            pl-=1
        count+=1
        
    print(count)           
    return count
solution(	[70, 80, 50], 100)