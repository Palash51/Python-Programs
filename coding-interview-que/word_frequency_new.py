def word_freq(strng):
	#strng = strng.isalnum()
	strng = strng.replace(' ', '').lower()

	if len(strng) == 0:
		print "No string Found"

	else:
		count = {}
		for letter in strng:
			if letter in count:
				count[letter] += 1

			else:
				count[letter] = 1


	return count

print(word_freq("google.com"))
