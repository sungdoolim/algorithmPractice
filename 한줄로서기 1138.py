
n=int(input())
memo=list(map(int,input().split()))
#print(memo)
result=[0]*n
for i in range(n):
    count=0
    jump=0
    while True:
        
        index=count+jump
        if count==memo[i]:
            if result[index]==0:
                result[index]=i+1
                break
            else:
                jump+=1

        elif result[index]==0:
            count+=1
        else:
            jump+=1
#print(result)
for i in result:
    print(i,end=" ")


