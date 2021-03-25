
def solution(numbers):
    num=list(map(str,numbers))
    answer=[]
    num.sort(key=lambda x:(x[0],x[1%len(x)],x[2%len(x)],x[3%len(x)]),reverse=True)

    answer=""
    for i in num:
        answer+=i



    return answer
solution(	[3, 30, 34, 5, 9])
