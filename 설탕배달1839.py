a=int(input())
count=0
while True:
    if a%5==0:
        print(count+int(a/5))
        break;
    else:
        a-=3
        count+=1
        if a==0:
            print(count)
            break;
        elif a<0:
            print(-1)
            break;
        
