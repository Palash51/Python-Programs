
l = [x for x in range(10) if x % 2 == 0]
print(l)

m = filter(lambda x:x % 2 == 0, [x for x in range(10)] )
# print(list(m))

o = map(lambda x: x**2, m)
print(list(o))

# p = reduce(lambda x,y:x+y, o)
# print(p)