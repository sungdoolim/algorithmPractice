
import math
n,k=map(int,input().split())
girls=[]
boys=[]
children=[]
for _ in range(n):
    a,b=map(int,input().split())
    if b<3:
        children.append(b)

    elif a==0:
        girls.append(b)
    else:
        boys.append(b)
cl=len(children)
resultcl=math.ceil(cl/k)
blm=0
glm=0
glh=0
blh=0
for i in boys:
    if i<5:
        blm+=1
    else:
        blh+=1
for i in girls:
    if i<5:
        glm+=1
    else:
        glh+=1
#print(glm,glh,blm,blh,cl)
print(math.ceil(glm/k)+math.ceil(glh/k)+math.ceil(blm/k)+math.ceil(blh/k)+resultcl)


