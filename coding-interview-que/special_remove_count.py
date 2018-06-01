def text_cleanup(text):
    new = ""
    for i in text:
        if i not in "?,.!/;:@#$%":
            new += i
    new = new.replace(' ', '').lower()
    count = {}
    for letter in new:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1


    return count

print text_cleanup('palas!@h patidar')


	 
	

