from collections import deque
n=int(input())
for _ in range(n):
    s=list(input())
    left,right=[],[]
    for i in s:
        #print(left,right)
        if i=="<":
            if left:
                right.append(left.pop())

        elif i==">":
            if right:
                left.append(right.pop())

        elif i=="-":
            
            
            if left:
                left.pop()

        else:
            left.append(i)
    for i in left:
        print(i,end="")
    right.reverse()
    for j in right:
        print(j,end="")
