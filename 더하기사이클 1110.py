n=int(input())
count=0
# if n<10:
#     pass
# else :
tmp=n
while True:
    count+=1
    tmp1=tmp%10
    tmp2=tmp//10
    tmp3=(tmp1+tmp2)%10
    tmp1*=10
    tmp=tmp1+tmp3
    #print(tmp)
    if tmp==n:
        print(count)
        break