for i in range(1, 10):
    print "i = ", i
    for j in range(1, 11):
        s_num = str(i * j)
        print(" " * (2- len(s_num)) + s_num)
    print " "
