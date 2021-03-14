import sys
ar=[]
n=int(sys.stdin.readline().rstrip())
for _ in range(n):
    ar.append(list(map(int,sys.stdin.readline().rstrip().split())))
# for i in ar:
#     print(i)
count1=0
count0=0
def conquer(start,end,start2,end2):
    global count1,count0
    value=ar[start][start2]
    # print(count1,count0)
    # print(start,end,start2,end2)
    if start>=end-1 or start2>=end2-1:
        if value==1:
            count1+=1
        else:
            count0+=1
        return
    for i in range(start,end):
        for j in range(start2,end2):
            if value!=ar[i][j]:
                conquer(start,(start+end)//2,start2,(start2+end2)//2)
                conquer((start+end)//2,end,start2,(start2+end2)//2)
                conquer(start,(start+end)//2,(start2+end2)//2,end2)
                conquer((start+end)//2,end,(start2+end2)//2,end2)
                return
    if value==1:
        count1+=1
    else:
        count0+=1
conquer(0,n,0,n)
print(count0)
print(count1)
