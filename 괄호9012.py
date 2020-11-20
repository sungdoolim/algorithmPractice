n=int(input())
l=[]
for i in range(n):
    l.append(input())

st=[]
for i in l:
    st.clear()
    for k in range(len(i)):
        if i[k]=="(":
            st.append(1)
        else:
            st.append(-1)
    count=0



        
    for q in st:
        count+=q
        if count<0:
            break;
    if count==0:
        print("YES")
    else:
        print("NO")
    
