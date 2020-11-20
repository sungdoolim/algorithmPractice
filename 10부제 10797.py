n=input()
import sys
a=list(map(str,sys.stdin.readline().split()))
count=0
for i in a:
    l=len(i)
    if i[l-1]==n:
        count+=1
print(count)

