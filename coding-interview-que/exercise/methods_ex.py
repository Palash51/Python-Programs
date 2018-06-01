class MyClass:
    def method(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'


# obj = MyClass()
# print(obj.method())
# #('instance method called', <MyClass instance at 0x101a2f4c8>)


# print(obj.classmethod())

# print(obj.staticmethod())


#obj = MyClass()
print(MyClass.method())
#('instance method called', <MyClass instance at 0x101a2f4c8>)


print(MyClass.classmethod())

print(MyClass.staticmethod())
