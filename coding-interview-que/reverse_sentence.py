# class UserMainCode(object):

# 	@classmethod
# 	def sen_rev(cls, strng):
# 		s = ''
# 		new_str = strng.split()
# 		for i in new_str:
# 			i = i.replace(i[-1], i[-1].upper())
# 			s = s + i + " "
# 		return s[::-1]


# strng = input()

# U = UserMainCode()
# print(U.sen_rev(strng))

# # print(sen_rev("palash patidar"))


class UserMainCode(object):

	@classmethod
	def count_cosecutive(cls, inp1, inp2):
		""""""
		c = 1
		inp2 = sorted(inp2)
		# print(inp2)
		for i in range(1,inp1):
			print(inp2[i])
			if (inp2[i] - inp2[i-1]) == 1:
				c = c + 1
		print(c)

inp1 = int(input())
inp2 = list(map(int, input().split()))
U = UserMainCode()

(U.count_cosecutive(inp1, inp2))