'''string = "Special $#! characters   spaces 888323"
a =  ' '.join(e for e in string if e.isalnum())
print(a)
'''


def text_cleanup(text):
    new = ""
    for i in text:
        if i not in "?,.!/;:@#$%":
            new += i
    return new
#strng = "pal@#$%as!h pa!.ti@#d,:a!r"
strng = open('a.txt').read()
print(text_cleanup(strng))

'''
def in_whitelist(character):
    return character.isalnum() or character in ['\\','/']
line2 = ''.join(e for e in line2 if in_whitelist(e))
print(in_whitelist("pal@#$%as!h"))
'''