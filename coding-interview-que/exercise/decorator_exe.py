def div_fun(fun):
  def inner(a,b):
      print("divide",a,"and",b)
      if b == 0:
         print("cannot divide")
         return
      x = a/b
      print(x)
      return fun(a,b)
  return inner

@div_fun
def divide(a,b):
    print("\noperation completed")

print(divide(4,2))

####################################

# class Decorator(object):

#   def __init__(self, func):
#     self.func = func

#   def __call__(self, *args, **kwargs):
#     print("before func call")
#     res = self.func(*args, **kwargs)
#     print("after func call")
#     return res

# @Decorator
# def testfunc():
#   print("inside the func")


# testfunc()




################## __int__ and __call__ ########
# class A:
#   def __init__(self):
#     print("init")
         
#   def __call__(self):
#     print("call")

# a=A()
# a()