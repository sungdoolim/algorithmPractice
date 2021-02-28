
import sys

tn=int(sys.stdin.readline().rstrip())
for _ in range(tn):
    casen=int(sys.stdin.readline().rstrip())
    ar=list(map(int,sys.stdin.readline().rstrip().split()))
    br=list(map(int,sys.stdin.readline().rstrip().split()))
    resulta=[0]*(casen)
    resultb=[0]*(casen)
    
    resulta[0]=ar[0]
    resultb[0]=br[0]
    
    if casen>1:
        resultb[1]=ar[0]+br[1]
        resulta[1]=br[0]+ar[1]
    for i in range(2,casen):
        resulta[i]=max(resultb[i-1]+ar[i],resultb[i-2]+ar[i])
        resultb[i]=max(resulta[i-1]+br[i],resulta[i-2]+br[i])

    print(max(resulta[-1],resultb[-1]))



            

            



    



# q=int(input())
# realresult=[]
# for _ in range(q):
#     n=int(input())
#     ar=[]
#     result=[0]*(n+1)
#     ar.append(list(map(int,input().split())))
#     ar.append(list(map(int,input().split())))
#     ckl=False
#    # print(ar)
#     #print(result)
#     if n==1:
        
#         realresult.append(max(ar[0][0],ar[1][0]))
#     elif n==2:
#         realresult.append(max(ar[0][0]+ar[1][1],ar[0][1]+ar[1][0]))
       
        
#     else:
        
#         if ar[0][0]>ar[1][0]:
#             result[1]=ar[0][0]
#         else:
#             result[1]=ar[1][0]
        
#         if ar[0][0]+ar[1][1]>ar[0][1]+ar[1][0]:
#             result[2]=ar[0][0]+ar[1][1]
#         else:
#             result[2]=ar[0][1]+ar[1][0]
#             ckl=True
        
#         for i in range(2,n):
#             k=0
#             if ckl:
#                 k=result[i]+ar[1][i]
#                 k2=result[i-1]+ar[0][i]
#                 if k> k2:
#                     ckl=not ckl
#                     result[i+1]=k
#                 else:
#                     result[i+1]=k2
#             else:
#                 k=result[i]+ar[0][i]
#                 k2=result[i-1]+ar[1][i]
#                 if k> k2:
#                     ckl=not ckl
#                     result[i+1]=k
#                 else:
#                     result[i+1]=k2
#     #print(result)
#         realresult.append(result[n])
            
# for i in realresult:
#     print(i)



