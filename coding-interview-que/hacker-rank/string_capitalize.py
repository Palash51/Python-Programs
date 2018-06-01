def capitalize(string):
	lst = string[:].split()
	for ch in lst:
		string = string.replace(ch, ch.capitalize())

	return string

if __name__ == '__main__':
    string = input()
    capitalized_string = capitalize(string)
    print(capitalized_string)


