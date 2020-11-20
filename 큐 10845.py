import sys
n=int(sys.stdin.readline().rstrip())
stack=[]

for i in range(n):
    cmd=sys.stdin.readline().rstrip()
    if "push " in cmd:
        cmd=int(cmd.split("push")[1])
        stack.append(cmd)

    elif "front"==cmd:
        #print(stack)
        if len(stack)==0:
            print(-1)
        else:
            print(stack[0])
    elif "back"==cmd:
        #print(stack)
        if len(stack)==0:
            print(-1)
        else:
            print(stack[len(stack)-1])       

    elif "size"==cmd:
        print(len(stack))

    elif "empty"==cmd:
        if len(stack)==0:
            print(1)
        else:
            print(0)

    else:
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop(0))


            


