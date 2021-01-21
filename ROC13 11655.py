string=input()
def ROC13(string):
    l=len(string)
    newstring=""
    for i in range(l):
        # print(i)
        # print(ord(string[i]))
        # print(ord(string[i])+13)
        # print(chr(ord(string[i])+13))
        k=ord(string[i])
        if k>109:
            newstring+=chr(k-13)
        elif 96<k<=109:
            newstring+=chr(k+13)
        elif 64<k<=77:
            newstring+=chr(k+13)
        elif k>77:
            newstring+=chr(k-13)
        else:
            newstring+=string[i]

        
    print(newstring)
ROC13(string)