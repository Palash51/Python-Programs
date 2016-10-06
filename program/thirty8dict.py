d={}
n = input()
d = [ map(str,raw_input().split()) for x in range(n)]


#print dict(d)

#for key, value in d.items():
 #   print "%s=%s" % (key, value)

for key,val in d:
    print("{} = {}".format(key, val))
    for i in range(n):
        name = raw_input()
    if name == key:
        print "found"
