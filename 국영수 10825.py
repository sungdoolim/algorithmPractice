import sys

n=int(sys.stdin.readline().rstrip())
ar=[]
for _ in range(n):
    name,language,english,math=sys.stdin.readline().rstrip().split()
    ar.append([name,int(language),int(english),int(math)])
ar.sort(key=lambda x:(-x[1],x[2],-x[3],x[0]))
for i in ar:
    print(i[0])