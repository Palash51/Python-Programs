'''def sen_rev(strng):
	new_str = []
	for i in range(len(strng)):
		if strng[i] == ' ':
			print strng[ :i]
		i = i + 1

	

sen_rev("palash patidar india ")'''

'''def rev_word1(s):
	#return " ".join(reversed(s.split()))
	return " ".join(s.split()[::-1])

print rev_word1("palash patidar india")'''
'''
def rev_word(s):

	words = []
	length = len(s)
	spaces = [' ']

	i = 0
	while i < length:
		if s[i] not in spaces:
			word_start = i
			while i < length and s[i] not in spaces:
				i += 1

			words.append(s[word_start:i])

		i += 1

	return " ".join(reversed(words))

print rev_word("palash patidar india won")'''




def rev_word(s):

	words = []

	i = 0
	while i < len(s):
		if s[i] not in ' ':
			word_start = i
			while i < len(s) and s[i] not in ' ':
				i += 1

			words.append(s[word_start:i])

		i += 1

	return " ".join(reversed(words))

print rev_word("palash patidar india won")





























