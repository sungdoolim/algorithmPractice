import sys
# sys.stdin.readline().rstrip().split()
n=int(sys.stdin.readline().rstrip())
ar=[]
for _ in range(n):
    ar.append(int(sys.stdin.readline().rstrip()))
result=[0]*1000001
result[1]=1
result[2]=2
result[3]=4
result[4]=7
for i in range(5,1000001):
    result[i]=(result[i-1]*2-result[i-4])%1000000009

# for j in range(11):
#     print(result[j])
for i in ar:
    print(result[i]) 
