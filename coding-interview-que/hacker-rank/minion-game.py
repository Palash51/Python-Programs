def minion_game(s):
	vowels = 'AEIOU'
	stuart = 0
	kevin = 0
	l = len(s)
	for i in range(l):  
		if s[i] in vowels:
			kevin += l - i
		else:
			stuart += l - i
        
	if stuart > kevin:
	    print('Stuart ', stuart)
	elif stuart == kevin:
	    print('Draw')
	else:
	    print('Kevin ', kevin)

minion_game("BANANA")