n=int(input())
ar=[]
br=[0]*26
for _ in range(n):
    ar.append(input())
for i in ar:
    il=len(i)
    for l in range(il):
        if i[l]=="A":
            br[0]+=10**(il-l)
        elif i[l]=="B":
            br[1]+=10**(il-l)
        elif i[l]=="C":
            br[2]+=10**(il-l)
        elif i[l]=="D":
            br[3]+=10**(il-l)
        elif i[l]=="E":
            br[4]+=10**(il-l)
        elif i[l]=="F":
            br[5]+=10**(il-l)
        elif i[l]=="G":
            br[6]+=10**(il-l)
        elif i[l]=="H":
            br[7]+=10**(il-l)
        elif i[l]=="I":
            br[8]+=10**(il-l)
        elif i[l]=="J":
            br[9]+=10**(il-l)
        elif i[l]=="K":
            br[10]+=10**(il-l)
        elif i[l]=="L":
            br[11]+=10**(il-l)
        elif i[l]=="M":
            br[12]+=10**(il-l)
        elif i[l]=="N":
            br[13]+=10**(il-l)
        elif i[l]=="O":
            br[14]+=10**(il-l)
        elif i[l]=="P":
            br[15]+=10**(il-l)
        elif i[l]=="Q":
            br[16]+=10**(il-l)
        elif i[l]=="R":
            br[17]+=10**(il-l)
        elif i[l]=="S":
            br[18]+=10**(il-l)
        elif i[l]=="T":
            br[19]+=10**(il-l)
        elif i[l]=="U":
            br[20]+=10**(il-l)
        elif i[l]=="V":
            br[21]+=10**(il-l)
        elif i[l]=="W":
            br[22]+=10**(il-l)
        elif i[l]=="X":
            br[23]+=10**(il-l)
        elif i[l]=="Y":
            br[24]+=10**(il-l)
        elif i[l]=="Z":
            br[25]+=10**(il-l)
            
count=9
while True:
    br[br.index(max(br))]=count
    count-=1
    if max(br)==9:
        break

#print(br)
s=0
for i in ar:
    il=len(i)
    
    for j in range(il):
        s+=(10**(il-j-1))*br[ord(i[j])-65]
print(s)