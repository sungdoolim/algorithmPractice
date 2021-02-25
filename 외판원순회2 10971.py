import sys

n=int(sys.stdin.readline().rstrip())

ar=[]
for _ in range(n):
    ar.append(list(map(int,sys.stdin.readline().rstrip().split())))
ckl=[0]*n
M=11000001
def dfs(s,ck,start,cur=0):
    #print(cur)
    global n,M
    b=False
    #curmoney=cur
    for i in range(n):
        if ck[i]==0 and ar[s][i]!=0:
            b=True
            ck[i]=1
            dfs(i,ck,start,cur+ar[s][i])
            ck[i]=0
    if (not b) and ar[s][start]!=0 and 0 not in ck:
        
        M=min(M,cur+ar[s][start])
        # print("M=",M)
for i in range(len(ar)):
    ckl[i]=1
    dfs(i,ckl,i)
    ckl[i]=0
print(M)
