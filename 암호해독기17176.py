n=int(input())

ar=list(map(int,input().split()))
k=(list(input()))
result=[]
for i in ar:
    if i==0:
        result.append(" ")
    elif 1<=i<=26:
        result.append(chr(i+64))
    else:
        result.append(chr(i+70))


result.sort()
k.sort()
# print(result)
# print(k)
bo=k==result
# for i in k:
#     if i not in r:
#         bo=False
#         break
#a=result&k
# print(a)
# if len(a)!=len(k):
#    bo=False

if bo:
    print("y")
else:
    print("n")