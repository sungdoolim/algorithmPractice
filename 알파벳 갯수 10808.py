import sys
a=sys.stdin.readline().rstrip()
result=[0]*26
l=len(a)
for i in range(l):
    #print(ord(a[i]))
    result[ord(a[i])-97]+=1
for i in result:
    print(i,end=" ")
