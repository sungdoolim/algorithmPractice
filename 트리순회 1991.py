n=int(input())
tree={}
for _ in range(n):
    a,b,c=input().split()
    tree[a]=[b,c]

def pre(a):
    if a!=".":
        print(a,end="")
        pre(tree[a][0])
        pre(tree[a][1])
def inorder(a):
    if a!=".":
        inorder(tree[a][0])
    
        print(a,end="")
        inorder(tree[a][1])

def post(a):
    if a!=".":
        post(tree[a][0])
        post(tree[a][1])
    
        print(a,end="")
pre("A")
print()
inorder("A")
print()
post("A")

