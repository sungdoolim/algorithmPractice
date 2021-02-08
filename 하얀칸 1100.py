ar=[]
for _ in range(8):
    ar.append(list(input().split()))
#print(ar)
l=len(ar)
count=0
for i in range(l):
    tmp=ar[i][0]
    #print(tmp)
    if not i%2:
        for j in range(0,8,2):
            if tmp[j]=='F':
                count+=1
    else:
        for j in range(1,8,2):
            if tmp[j]=='F':
                count+=1
    
print(count)