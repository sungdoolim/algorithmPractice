# 숫자카드 10815
import sys
def divi(i,start,end):
    #print("start : ",start,"end : ",end)
    mid=int((start+end)//2)
    global c
    if start>=end:
        #print(start,end,a[start])
        if i==a[start]or i==a[end]:
            result[c]=1
        else:
            result[c]=0
        c+=1
        
        #print(result,c-1)
        return 1
    elif i==a[mid]:
          result[c]=1
          c+=1
          return 1
    elif i<a[mid]:
        #print(start,mid-1)
        divi(i,start,mid-1)
        
    else:
        #print(mid+1,end)
        divi(i,mid+1,end)
        

    return 0;
global n,m,a,b,c
n=int(sys.stdin.readline())

a=list(map(int,sys.stdin.readline().split()))
a.sort()
#print(a)
m=int(input())

b=list(map(int,input().split()))
#print(b)
result=[0]*m
c=0
for i in b:
    divi(i,0,n-1)
#print(result)
for i in result:
    print(i,end=" ")

