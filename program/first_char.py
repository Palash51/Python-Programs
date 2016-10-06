#import string
def first(st):
    new = [st[0]]
    for i in range(len(st)):
        if st[i] == ' ':
            new.append(st[i+1])
    #return new
    b = "".join(new)
    print b.replace(" ","")



st = " palash    pati   dar chennai "
first(st)

'''
f= "   pal hio   kl lihu"#raw_input("Enter")
print "".join(item[0].lower() for item in f.split())
'''
