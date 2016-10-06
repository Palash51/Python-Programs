'''class Joe(object):
    greeting = "hello, joe"  #string

thisjoe = Joe()

print thisjoe.greeting
'''

'''class Joe(object):
    def callme(self):
        print("calling 'callme' method with instance: ")
        print(self)
        
thisjoe = Joe()

print thisjoe.callme()
'''
'''#instance attribute
import random

class Myclass(object):
    def dothis(self):
        self.rand_val = random.randint(1,10)
        

myinst = Myclass()
myinst.dothis()
print(myinst.rand_val)
'''

#encapsulation

'''class Myclass(object):
    def set_val(self, val):
        self.value = val

    def get_val(self):
        return self.value


a = Myclass()
b = Myclass()

a.set_val(10)
b.set_val(100)

print(a.get_val())
print(b.get_val())
'''
#encapsulation
'''
class MyInteger(object):
    def set_val(self, val):
        try:
            val = int(val)
        except ValueError:
            return
        self.val = val

    def get_val(self):
        return self.val

    def increment_val(self):
        self.val = self.val + 1

i = MyInteger()
i.set_val(9)
print i.get_val()
i.get_val()
print i.gert_val()
'''
#init constructor
'''
class MyNum(object):
    def __init__(self, value): #private method magic init called automatc when new method instance is creatred
        print "calling __init__"
        self.val = value #constr

    def increment(self):
        self.val = self.val + 1

dd = MyNum(5)
dd.increment()
dd.increment()
print dd.val
'''

#class attributes
'''
class YourClass(object):
    classy = 10  #class variable

    def set_val(self):
        self.insty = 100 #attribute

dd = YourCalss()

dd.set_val()
print(dd.classy)
print(dd.insty)
'''

#working with class

class InstanceCounter(object):
    count = 0 #class variable , class attr

    def __init__(self, value):
        self.val = val
        InstanceCounter.count +=1

    def set_val(self, newval):
        self.val = newval

    def get_val(self):
        return self.val

    def get_count(self):
        return InstanceCounter.count


a = InstanceCounter(5)
b = InstanceCounter(13)
c = InstanceCounter(17)

for obj in (q, b, c):
    print "val of obj: %s" %(obj.get_val()) # initialize value (5, 13, etc)
    print "count: %s" %(obj.get_count())
    
 






















































































