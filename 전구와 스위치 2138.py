import sys
r=sys.stdin.readline
n=int(r().rstrip())
ar=list(map(int,list(r().rstrip())))# 원 상태 전구 저장
ar2=ar.copy()
result=list(map(int,list(r().rstrip())))# 목표 상태 전구 저장
countNoZeroSwitch=0# 맨 처음 버튼을 누르고 시작 했을 때
countZeroSwitch=0# 맨 처음 버튼을 누르지 않고 시작 했을 때
resultCount=1000001

ar[0]=1 if ar[0]==0 else 0
ar[1]=1 if ar[1]==0 else 0
countZeroSwitch+=1
# 처음 버튼을 누르고 시작합니다

if n!=2:
    for i in range(1,n-1):
        if ar[i-1]==result[i-1]:
            # 기준이 되는 비교는 i-1번째 입니다. for문이 실행되며 더이상 바꿀 수 없는 값이 되기 때문 입니다
            continue
        else:
            # 버튼을 눌렀을 때의 결과
            ar[i]=1 if ar[i]==0 else 0
            ar[i+1]=1 if ar[i+1]==0 else 0  
            ar[i-1]=1 if ar[i-1]==0 else 0
            countZeroSwitch+=1
           # print(ar)

if ar[n-2]!=result[n-2]:# 마지막 순선의 버튼을 누를지를 결정합니다
    ar[n-2]=1 if ar[n-2]==0 else 0
    ar[n-1]=1 if ar[n-1]==0 else 0
    countZeroSwitch+=1
if ar==result:# 목표상태와 원 상태가 같다면 resultCount로 저장합니다
    resultCount=countZeroSwitch

    

# 처음 버튼을 누르지 않았을 때 입니다. 위의 설명과 같습니다. 
if n!=2:
    for i in range(1,n-1):
        if ar2[i-1]==result[i-1]:
            continue
        else:
            ar2[i]=1 if ar2[i]==0 else 0
            ar2[i+1]=1 if ar2[i+1]==0 else 0  
            ar2[i-1]=1 if ar2[i-1]==0 else 0
            countNoZeroSwitch+=1
           # print(ar)

if ar2[n-2]!=result[n-2]:
    ar2[n-2]=1 if ar2[n-2]==0 else 0
    ar2[n-1]=1 if ar2[n-1]==0 else 0
    countNoZeroSwitch+=1


if ar2==result:# 목표결과와 같다면 최솟값을 resultCount로 합니다
    resultCount=min(resultCount,countNoZeroSwitch)
if resultCount==1000001:
    print(-1)
else:
    print(resultCount)