# tutorial 1 -- 
# ---- creating classses and 
# ---- defining objects and 
# ---- adding attributes of class

class Test:
	pass

class Point:
	pass


p1 = Point() # defining object
p1.x = 2 # attributes of a class
p1.y = 3
p1.z = 5

p2 = Point()
p2.x = 4 # attributes of a class
p2.y = -2
p2.z = 7


print(p1.x,p1.y,p1.z) # address of obj in memory
print(p2.x,p2.y,p2.z)


t1 = Test()
t1.text = 'Hello py'  # member variable of class
t1.var = 3.14

print(t1.text, t1.var)

