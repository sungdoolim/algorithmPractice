import sys


photon=int(sys.stdin.readline().rstrip())
studentn=sys.stdin.readline().rstrip()
recommend=list(map(int,sys.stdin.readline().rstrip().split()))

candidate=[0]*(photon)
recommendn=[100000]*(photon)
time=[0]*(photon)
def timeplus():
    for i in range(len(time)):
        time[i]+=1
for i in recommend:
    if i in candidate:
        index=candidate.index(i)
        recommendn[index]+=1
        #time[index]+=1
    elif 0 in candidate:
        index=candidate.index(0)
        candidate[index]=i
        recommendn[index]=1
        time[index]=1
    elif recommendn.count(min(recommendn))>1:
        m=min(recommendn)
        tmp=[]
        for j in range(photon):
            if recommendn[j]==m:
                tmp.append(j)
        mintime=0
        for j in tmp:
            mintime=max(mintime,time[j])
        index=time.index(mintime)
        candidate[index]=i
        recommendn[index]=1
        time[index]=1
    else:
        index=recommendn.index(min(recommendn))
        candidate[index]=i
        recommendn[index]=1
        time[index]=1
    timeplus()
   # print(candidate)
candidate.sort()
for i in candidate:
    print(i,end=" ")
        