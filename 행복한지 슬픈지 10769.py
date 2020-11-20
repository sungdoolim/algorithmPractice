
n=input()
sad=":-("
happy=":-)"
sadar=n.split(sad)
#print(sadar)
sadcount=len(sadar)
happyar=n.split(happy)
#print(happyar)
happycount=len(happyar)
#print(sadcount,happycount)

if sadcount==1 and happycount==1:
    print("none")
elif sadcount>happycount:
    print("sad")
elif sadcount==happycount:
    print("unsure")
else:
    print("happy")
