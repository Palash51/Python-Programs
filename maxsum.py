# #a = [-1,2,-2,4,-3,10] [1,2,-1,3,4,10,10,-10,-1]# 7

# def max_count(arr):
# 	if len(arr) == 0:
# 		return 0

# 	curr_sum = arr[0]
# 	max_sum = curr_sum
# 	for i in arr[1:]:
# 		curr_sum = max(curr_sum+i, i)
# 		max_sum = max(curr_sum,max_sum)
		

# 	print max_sum

# new = []
# a = [-2, -3, 4, -1, -2, 1, 5, -3]
# max_count(a)

def subArraySum(A):
  m = [0] * len(A)
  startingIndex = len(A) - 1
  endingIndex = 0
 
  # find endingIndex
  m[0] = A[0]
  for  i in range(1, len(A)):
    m[i] = max(A[i], m[i - 1] + A[i])
    if (m[endingIndex] < m[i]):
      endingIndex = i
 
  # find startingIndex
  m = [0] * len(A)
  m[len( A ) - 1] = A[len( A ) - 1]
  for i in range( len( A ) - 2, -1, -1 ):
    m[i] = max( A[i], m[i + 1] + A[i] )
    if m[startingIndex] < m[i]:
      startingIndex = i
 
  if endingIndex <= startingIndex:
    return None # no array size less than 2 allowed
 
  result = A[startingIndex:endingIndex + 1]
 
  return result
print subArraySum([-2, -3, 4, -1, -2, 1, 5, -3])