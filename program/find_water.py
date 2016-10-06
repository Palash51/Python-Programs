def water_collected(heights):
    water_collected = 0
    left_height = []
    right_height = []

    temp_max = heights[0]
    for height in heights:
        if (height > temp_max):
            temp_max = height
        left_height.append(temp_max)

    temp_max = heights[-1]
    for height in reversed(heights):
        if (height > temp_max):
            temp_max = height
        right_height.insert(0, temp_max)

    for i, height in enumerate(heights):
        water_collected += min(left_height[i], right_height[i]) - height
    return water_collected

arr = [0,1,0,2,1,0,1,3,2,1,2,1]
#n = len(arr)
print water_collected(arr)




'''
def findwater(arr,n):
    water = 0
    left= []
    right = []
    #left[0] = arr[0]
    for i in range(1,n-1):
        left[i] = max(left[i-1], arr[i])

    right[n-1] = arr[n-1]
    for i in range(n-2):
        right[i] = max(right[i+1],arr[i])
        i = i - 1
    

    for i in range(n):
        water += min(left[i],right[i]) - arr[i]

    return water

arr = [0,1,0,2,1,0,1,3,2,1,2,1]
n = len(arr)
print findwater(arr,n)
'''
'''
class Solution:
    # @param {integer[]} height
    # @return {integer}
    def trap(self, height):
        
        if not height or len(height)==1:
            return 0

            
        max_left =  height[0]   
        AddVolume = [max_left]
        
        for i in range(1,len(height)-1):
            if max_left < height[i-1]:
                max_left = height[i-1]
            AddVolume.append(max_left)

        max_right = height[-1]        
        AddVolume.append(max_right)
        
        for i in reversed(range(1,len(height)-1)):
            if max_right < height[i+1]:
                max_right = height[i+1]
            AddVolume[i] = min(max_right,AddVolume[i])
        
        for i in range(len(AddVolume)):
            AddVolume[i] = max(AddVolume[i] - height[i],0)
        
        return sum(AddVolume)


s = Solution
lst = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print s.trap(lst)
'''
