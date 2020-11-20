#잃어버린 괄호 1541
a=input().split('-')
#ism=a[0]=='-'
#print(ism)
#print(a,b)

l=len(a)
result=[]
m=0

for i in a:
    result.append(eval(i))
for i in result:
    m+=i
print(2*result[0]-m)
#print(result)
