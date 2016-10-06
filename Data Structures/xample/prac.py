def answer(arr, cha_list):
        len_chant = len(cha_list)
        if len_chant < arr[0] or len_chant < arr[1]:
                if len_chant < arr[0]:
                        arr[0] =  arr[0]%len_chant - 1
                if len_chant < arr[1]:
                        arr[1] =  arr[1]%len_chant - 1
                if cha_list[arr[0]] == cha_list[arr[1]]:
                        return "Yes"
                else:
                        return "No"
        else:
                if cha_list[arr[0]-1] == cha_list[arr[1]-1]:
                        return "Yes"
                else:
                        return "No"

chant = raw_input()
chant_list = list(chant)
case = int(raw_input())
num = []
#ktar = []
#for i in range(case):
while case > 0:
        n = raw_input()
        num.extend([int(j) for j in n.split(" ")])
        #ktar.append(answer(num ,chant_list))
        #num = []
        #case -= 1
#for j in ktar:
        #print j      
        print answer(num ,chant_list)
        num = []
        case -= 1