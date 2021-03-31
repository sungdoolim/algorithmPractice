

def solution(genres, plays):
    answer = []
    count=0
    genpl={}
    name={}
    for gen,play in zip(genres,plays):
        #print(gen,play)
        
        if gen in genpl:
            genpl[gen].append([play,count])
            name[gen]+=play
        else:
            genpl[gen]=[[play,count]]
            name[gen]=play
        count+=1
        
    genlist=list(genpl.items())
    
  #  print(genlist)
    #genlist.sort(key=lambda x:x[1])
    # for i in genlist:
    #     print(i)
    
    namlist=list(name.items())
    namlist.sort(key=lambda x:-x[1])
    result=[]
    for j in namlist:
        # print(j[0])
        # print(genlist)
        ar=genpl[j[0]]
        ar.sort(key=lambda x:-x[0])
        c=0
        for j in ar:
            if c==2:
                break
            c+=1
            result.append(j[1])
    return (result)

    
        
   # print(genpl)
    




    return answer

solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500])

