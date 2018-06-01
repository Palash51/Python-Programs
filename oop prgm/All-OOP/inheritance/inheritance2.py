## tutorial -- inheritance
# -- inheritance is implicite
## -- issubclass(A,B)  return boolean

### class Person(object) --> it is explicit but in python3 no need to define it like this (implicit)
### by default class is a subclass of object class


class Person:
	pass

class Employee(Person):
	pass


def main():
	print(issubclass(Employee, Person))
	print(issubclass(Employee, object))
	print(issubclass(Employee, object))
	

if __name__ == "__main__":
	main()