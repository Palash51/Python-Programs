def isPangram(s):
    alphabetset = set('abcdefghijklmnopqrstuvwxyz')
    set_string = set(s.lower())
    return set_string.issuperset(alphabetset)


str1 = "aabcdefghijklmnopqrstuvwxyz"
print isPangram("str1")
