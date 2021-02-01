a,b=map(int,input().split())
ar=[]
br=[]
for _ in range(a):
    ar.append(list(map(int,list(input()))))
for _ in range(a):
    br.append(list(map(int,list(input()))))
count=0

# for i in ar:
#     print(i)
# print()
# for i in br:
#     print(i)

for i in range(a):
    for j in range(b):
        if ar[i][j]==br[i][j]:
            continue
        else:
            if i+2<a and j+2<b:
                count+=1
                for k in range(i,i+3):
                    for q in range(j,j+3):
                        ar[k][q]=abs(ar[k][q]-1)
# print()
# for i in ar:
#     print(i)
# print()
# for i in br:
#     print(i)

if ar==br:
    print(count)
else:
    print(-1)

