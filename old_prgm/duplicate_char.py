def dup_str(s):

	for i in range(len(s)):
		for j in range(i+1, len(s)):
			if s[j] == s[i]:
				return False


	return True

print dup_str("abcde")
