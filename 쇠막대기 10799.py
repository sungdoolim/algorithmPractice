from collections import deque
ar=deque(list(input()))
stac=[]
stac.append(ar.popleft())
count=1
result=0
while ar:
    value=ar.popleft()
    
    if value=="(":
        
        count+=1
    else:
        v=stac[-1]
        if v=="(":
            
            count-=1
            result+=count
       #     print(result)
        else:
            count-=1
            result+=1
    stac.append(value)
            
print(result)



