n=int(input())
areto=[0]*(n+2)
areto[0]=1
areto[1]=1
#sosu=[]
result=[]
for i in range(2,n+1):
    if areto[i]:
        
        pass
    else:
        j=2
#        sosu.append(i)
        while True:
            if n%i==0:
                result.append(i)
                n//=i
            else:
                break

        while True:
            if i*j>n:
                break
            areto[i*j]=1
            j+=1
        if n==1:
            break



# print(areto)
# print(sosu)
# print(result)
for i in result:
    print(i)