m,d=map(int,input().split())
ar=['SUN','MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
br=[0,31,28,31,30,31,30,31,31,30,31,30,31]
cr=[]
hap=0
for i in br:
    hap+=i
    cr.append(hap)
#print(cr)
def cal(m):
    result=cr[m-1]+d
    return ar[result%7]

if m==1:print(ar[d%7])  
elif m==2:print(cal(m))
elif m==3:print(cal(m))
elif m==4:print(cal(m))
elif m==5:print(cal(m))
elif m==6:print(cal(m))
elif m==7:print(cal(m))
elif m==8:print(cal(m))
elif m==9:print(cal(m))
elif m==10:print(cal(m))
elif m==11:print(cal(m))
elif m==12:print(cal(m))