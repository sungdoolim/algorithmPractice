import sys
#sys.stdin.readline().rstrip()
dic={}
n=int(sys.stdin.readline().rstrip())



for _ in range(n):
    s=int(sys.stdin.readline().rstrip())
    if s in dic:
        dic[s]+=1
    else:
        dic[s]=1
listdic=list(dic.items())
listdic.sort(key=lambda x:(-x[1],x[0]))
print(listdic[0][0])