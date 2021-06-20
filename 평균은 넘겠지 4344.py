n=int(input())
result=[]
ar=[]
for _ in range(n):
    ar.append(list(map(int,input().split())))
    
#print(ar)
for i in ar:
    count=0
    avr=(sum(i)-i[0])/i[0]
    for j in i[1:]:
        if j>avr:
            count+=1
    result.append(count/i[0]*100)
        

count=0

for i in result:

    print("%.3f"%i,end="%\n")