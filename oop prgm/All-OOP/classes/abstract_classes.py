## tutorial -- 
### --abstract class--
## class for which we do not create objects are called Abstract classes
## base class for abstration is ABC

from abc import ABC, abstractmethod

class Animal(ABC):
	
	@abstractmethod
	def move(self):
		pass


class Human(Animal):

	def move(self):
		print("I can move walk and run")

class Snake(Animal):

	def move(self):
		print("I can crawl")

def main():

	# a1 = Animal()

	h1 = Human()
	h1.move()

	s1 = Snake()
	s1.move()


if __name__ == '__main__':
	main()
