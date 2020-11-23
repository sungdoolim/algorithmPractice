from math import sqrt 
import sys
n=int(sys.stdin.readline().rstrip())
ar=[]
sqr=[]
count=0
ar=list(map(int,sys.stdin.readline().rstrip().split()))
result=[-1]*1001
result[0]=0
result[1]=0
result[2]=-1
def areto(i):
    if result[i]==-1:
        sq=int(sqrt(i))
        isa=True
        for j in range(3,sq+1):
            if i%j==0:
                result[i]=0
                isa=False
                break
        if isa:
            result[i]=1
    
        j=2
        while True:
            if i*j>1000:
                break
            if result[i*j]==-1:
                result[i*j]=0
                j+=1
            else:
                break
for i in range(2,len(result)):
    areto(i)



        
#print(result)
count=0
for re in ar:
    count+=result[re]
print(count)





# for i in range(l):
#     ish=True
#     j=int(sqr[i])
#     for k in range(2,j+1):
#         if ar[i]%k==0:
#             ish=False
            
#             break
#     if ish:
#         result.append(1)
#         count+=1
#     else:
#         result.append(0)

# #print(result)
# print(count)


