#x = int(raw_input("enter the no"))
#arr = []
arr = [int(i) for i in raw_input().split()]
#arr = int(raw_input("enter the no"))
for i in range(len(arr)):
    #for j in range(1, i+1):
        if arr[i] % arr[i+1] == 0:
            print "yes"
        else:
            print arr[i]
        
    
