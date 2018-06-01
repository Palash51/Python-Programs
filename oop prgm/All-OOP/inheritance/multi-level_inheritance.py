## tutorial -- multi-level inheritance

class Person:

	def assign_basic(self, name, age):
		self.name = name
		self.age = age



class Employee(Person):
	
	def assign_emp(self, eid):
		self.eid = eid

class Programmer(Employee):
	
	def assign_pro(self, lang):
		self.lang = lang


def main():
	p = Programmer()
	p.assign_basic("palash", 23)
	p.assign_emp("228")
	p.assign_pro("python3")
	print(p.name,p.age,p.eid,p.lang)



if __name__ == '__main__':
	main()

