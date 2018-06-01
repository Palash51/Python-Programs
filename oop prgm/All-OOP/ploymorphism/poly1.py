## tutorial -- polymorphism

# --ploymorphism-- ==> the ability to behave in  various forms

# overriding is a type of a ploymorphism

# overriding is when u call a method on an object and the
# method is subclass with the same signature as the one in superclass is called


### init method is overriding


###### super() ==> invoking the initializer of base class

class Person:

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    def __str__(self):
        return self.first + " " + self.last + " and age is - " + str(self.age)


class Employee(Person):

    # def __init__(self, first, last, age, sal):  ## without super()
    #     self.first = first
    #     self.last = last
    #     self.age = age
    #     self.sal = sal

    # def __init__(self, first, last, age, sal):   ### super() --1 
    # 	super().__init__(first, last, age)
    # 	self.sal = sal

    def __init__(self, first, last, age, sal):		### super() --2
    	super(Employee, self).__init__(first, last, age)
    	self.sal = sal


    # def __str__(self):
    #     return self.first + " " + self.last + " and age is - " + \
    #     str(self.age) + " salary is -" + str(self.sal)

    def __str__(self):
        return super().__str__ () + " salary is -" + str(self.sal)


def main():
    x = Person("palash", "patidar", 23)
    # print(x)

    y = Employee("chinu", "patidar", 21, 50000)
    # print(y)


# if __name__ == "__main__":
#     main()






#############################################################################



#################################################
# using keyword *args and **kwargs in super() method
##################################################
#20 major concepts


class Person:

    def __init__(self, *args, **kwargs):
        self.first = kwargs['name']
        self.last = kwargs['lname']
        self.age = kwargs['age']

    def __str__(self):
        return self.first + " " + self.last + "\nage : " + str(self.age)


class Employee(Person):

    def __init__(self, *args, **kwargs):
        super(Employee, self).__init__(*args, **kwargs)
        self.sal = kwargs['salary']
        self.eid = kwargs['eid']
        

    def __str__(self):
        return super().__str__ () + "\nemp id: "  + str(self.eid) + "\nsalary : " + str(self.sal)


def main():
    data = {'name':'chinu', 'lname':'patidar', 'age':'21', 'eid':'228', 'salary':'40000'}
    x = Person(**data)
    y = Employee(**data)
    # print(x)
    print(y)


if __name__ == "__main__":
    main()






