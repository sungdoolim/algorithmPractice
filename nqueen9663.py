n=int(input())
cols=[]
#print(cols)
count=0
def check(i,coll,col,l):
#col[l]=i가 들어가도 되?col[coll]이 있을때
    if i==col[coll] or abs((l-coll)/(i-col[coll]))==1 or col[coll]==i:
        return False
    return True
count=0
def btrac(col):
    candidate=[]
    global count
    l=len(col)
   # print("col : ",col)
    if l==n:
        count+=1
        return
    for i in range(n):  
        #print(i,l)
        b=True
        for j in range(l):
            b=check(i,j,col,l)
            if not b:
                break
        if b:
            candidate.append(i)
    #print(candidate)
    for i in candidate:
        cp=col.copy()
        cp.append(i)
        btrac(cp)

btrac(cols)
            
print(count)
            
