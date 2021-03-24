def solution(clothes):
    List=[]
    result=[]
    for cloth in clothes:
        name,part=cloth[0],cloth[1]
        if part not in List:
            List.append(part)
            result.append(1)
        else:
            result[List.index(part)]+=1


    r=1
    for i in result:
        r*=(i+1)
    print(r-1)


ar=		[["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
solution(ar)