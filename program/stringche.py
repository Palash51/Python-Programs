'''def is_pangram(phrase):
    phrase = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in phrase:
            return False


    return True

alphabet = raw_input()
#alphabet = "abcdefghijklmnopqrstuvwxyz"
print is_pangram(alphabet)
'''
#myPhrase = "The quick brown fox jumps over the lazy dog"
'''
def is_pangram(phrase):
    c = 0
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    phraseLetters = ""
    for char in phrase:
        for letter in alphabet:
            if char == letter and char not in phraseLetters:
                phraseLetters += char
    for char in phraseLetters:
        for letter in alphabet:
            if char == letter:
                c += 1
    if c == 26:
        return True
    else:
        
        return False

myPhrase = raw_input()
print is_pangram(myPhrase)
'''





text = raw_input()
s = set(text.lower())

if sum(1 for c in s if 96 < ord(c) < 123) == 26:
    print ('yes')
else:
    print ('no')



























