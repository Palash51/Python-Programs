############## basic example ###########

class Person(object):

    def __init__(self, name):
        self.name = name
 
    def getName(self):
        return self.name
 
    def isEmployee(self):
        return False
 
 
class Employee(Person):
 
    def isEmployee(self):
        return True
 
emp = Person("Geek1") 
#print(emp.getName(), emp.isEmployee())
 
emp = Employee("Geek2")
#print(emp.getName(), emp.isEmployee())

#print(issubclass(Employee, Person))


#################### create object of derived class u can access Base class properties ###
### using Base class name ###

class X(object):
    def __init__(self,a):
        self.num = a
    def doubleup(self):
        self.num *= 2
 
class Y(X):
    def __init__(self,a):
        X.__init__(self, a)
    def tripleup(self):
        self.num *= 3
 
obj = Y(4)
print(obj.num)
 
obj.doubleup()
print(obj.num)
 
obj.tripleup()
print(obj.num)

print(issubclass(Y,X))
print(isinstance(obj, X))

########################## using keyword super()  #########

class Person(object):
    def __init__(self, name):
        self.name = name
         
    def getName(self):
        return self.name
     
    def isEmployee(self):
        return False
 
class Employee(Person):
    def __init__(self, name, eid):
        super(Employee, self).__init__(name)
        self.empID = eid
         
    def isEmployee(self):
        return True
         
    def getID(self):
        return self.empID
 

emp = Employee("Geek1", "E101") 
#print(emp.getName(), emp.isEmployee(), emp.getID())