from collections import deque
def solution(numbers, target):
    global count

    count=0
    
    def dfs(num,ar,target):
        global count
        if ar:

            n=ar.pop()
            dfs(num+n,ar.copy(),target)
            dfs(num-n,ar,target)
        else:
            if num==target:
                count+=1

    num=numbers.pop()
    dfs(num,numbers.copy(),target)
    dfs(-num,numbers,target)

    print(count)
    answer = 0
    return count

solution([1, 1, 1, 1, 1], 3)