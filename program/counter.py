'''s='aaabbttcc'
c = Counter(s)

print (''.join (str (v) + k for k, v in c.items ()))
'''

def thing(string):
    buf = ""
    prev = ""
    count = 0

    for i in string:
        if not prev:
            prev = i
            count += 1 
        else:
            if i == prev:
                count += 1 
            else:
                buf += "{}{}".format(count, prev)
                count = 1
                prev = i
    buf += "{}{}".format(count, prev)
    print(buf)

thing("aaabbccc")
