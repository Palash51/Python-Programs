'''original = raw_input('Enter a word:')
word = original.lower()
first = word[0]

if len(original) > 0 and original.isalpha():
    if first in 'aeiou':
        print "vowel"
    else:
        print "consonant"
else:
    print "empty"
'''

def isVowel(letter):
   if letter == "a" or letter == "e" or \
      letter == "i" or letter == "o" or \
      letter == "u":
      return True
   else:
      return False

def numVowels(string):
   string = string.lower()
   count = 0
   for i in range(len(string)):
      if isVowel(string[i]):
         count += 1 #count = count + 1
   return count

print "Enter a string: "
strng = input()
print "There are " + str(numVowels(strng)) + " vowels in the string."
