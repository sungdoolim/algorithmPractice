def solution(brown, yellow):
    answer = []
    #brown+yellow=x*y
    #brown=2*x+2*y-4
    result=[]
    for i in range(1,brown//2):
        for j in range(1,brown//2):
            if i*j==brown+yellow and brown==2*i+2*j-4 and i>=j:
                result.append(i)
                result.append(j)
                return result
    print(result)




solution(8, 1)