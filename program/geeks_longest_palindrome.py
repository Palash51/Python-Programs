'''def palin(str1):
    front = []
    back = []
    i = 0
    j = len(str1)-1

    while(j>=i):
        if str1[i] == str1[j]:
            front.append(str1[i])
            

        i = i + 1
        j = j - 1






            
    print front

palin("forgeeksskeegfor")
'''


def palindromes(text):
    text = text.lower()
    results = []

    for i in range(len(text)):
        print i
        for j in range(0, i):
            print j
            palin = text[j:i + 1]

            if palin == palin[::-1]:
                results.append(palin)

    return text.index(max(results, key=len)),results
    print max(results, key=len)

print palindromes("forgeeksskeegfor")






a = [1,1,1,0,1,1,0,0,1,0,1]
m = []

for i in a:
    if i == 1:
        while i == 1:
            m.append(i)
            i = i + 1

    if i == 0:
        pass
    #i = i + 1
        

print m

    















