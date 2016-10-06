def median(midlist):
    midlist.sort()
    lens = len(midlist)
    if lens % 2 != 0: 
        midl = (lens / 2)
        res = midlist[midl]
    else:
        odd = (lens / 2) -1
        ev = (lens / 2) 
        res = float(midlist[odd] + midlist[ev]) / float(2)
    return res

#print median([1,2,3,4])
#nums = []
#n = raw_input()
#nums.extend([int(i) for i in n.split(" ")])
nums = list(map(int, raw_input().split()))
print median(nums)

'''
inp = list(map(int, raw_input().split()))
print inp
print inp[1] + inp[2]'''
 
