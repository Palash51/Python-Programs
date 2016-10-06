chant = raw_input()
chant_list = list(chant)
case = int(raw_input())
arr = []
while case > 0:
        n = raw_input()
        arr.extend([int(j) for j in n.split(" ")])     
        len_chant = len(chant)
        arr[0] =  arr[0]%len_chant
        arr[1] =  arr[1]%len_chant
        if chant[arr[0]-1] == chant[arr[1]-1]:
                print "Yes"
        else:
                print "No"
        arr = []
        case -= 1