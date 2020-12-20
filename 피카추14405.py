s=input()
l=len(s)
i=0
a=True
while a:
    a=False
    if s[i:i+2]=="pi" or s[i:i+2]=="ka":
        s=s[i+2:]
        #print(s)
        a=True
    elif s[i:i+3]=="chu":
        s=s[i+3:]
        a=True
if len(s)==0:
    print("YES")
else:
    print("NO")

