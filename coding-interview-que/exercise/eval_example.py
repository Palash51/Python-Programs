from math import *
 
def function_creator():
    expr = input("Enter the function(in terms of x):")
    x = int(input("Enter the value of x:"))
    y = eval(expr)
    print("y = {}".format(y))
 
if __name__ == "__main__":
    function_creator()