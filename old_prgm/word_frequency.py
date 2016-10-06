def text_cleanup(text):
    new = ""
    for i in text:
        if i not in "?,.!/;:@#$%":
            new += i
    new = new.replace(' ', '').lower()


	if len(new) == 0:
		print "No string Found"

	else:
		count = {}
		for letter in strng1:
			if letter in count:
				count[letter] += 1

			else:
				count[letter] = 1


	return count

print text_cleanup('palas!@h patidar')


	 
	

