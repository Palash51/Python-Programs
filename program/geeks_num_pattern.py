'''num = input()

for i in range(0,num):
    print i



def printTri(n):
    for i in range(1,n+1):
        print(' '.join(str(i)*(n+i)))

printTri(6)
'''

str1 = "WELCOMETOZOHOCORPORATION"

for i in range(len(str1)+1):
    print " ".join(str1[i] + '\n') 
