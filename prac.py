#file read
'''
file1 = open("pyt.txt", "r")
#print(file1.read())
print(file1.read())
print(file1.tell())
#print(position = file1.seek(0,0))
#pk = file1.read(18)
#print(pk)
'''

#file write

'''f = open("pyt.txt", "w")
#print(f.read)
print(f.write("i have entered some text in this file without opening this file this seems to be quite nice"))
print(f.close)
f = open("pyt.txt", "r")
print(f.read())
'''

#appending to file

'''
f = open("pyt.txt", "a")
print(f.write("\n\nthis is my appending text"))
f.close
f = open("pyt.txt", "r")
print(f.read())
'''

#copying files

ufn = input("enter your file name:")
file1 = open(ufn, "r")
ufn = ufn + ".txt"
file1 = open(ufn, "r")
file2 = open("copiedfile.txt", "w")
print(file2.write(file1.read()))
file1.close()
file2.close()
file2 = open("copied.txt", "r")
print(file2.read())

