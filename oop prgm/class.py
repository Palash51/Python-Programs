class myclass:
   sample=0
   w=0
   b=0
   g=0
   o=0
   color_list=['black','white','gray']
   def __inti__(self,name):
     myclass.name=name
     print("what's the color of your car?")
     myclas.color=input()
     myclass.sample=myclass.samaple+1
   def check_color(self):
     if myclass.color in myclass.color_list(color):
        if myclass.color==myclass.color_list[0]:
                myclass.b=myclass.b+1
        elif myclass.color==mymclass.color_list[1]:
            myclass.w=myclass.w+1
        else:
           myclass.g=myclass.g+1
     else:
         myclass.o=myclass.o+1
   def display_result(self):
      print("hello",myclass.name)
      print("total number of black cars:",myclass.b)
      print("total number of white cars:",myclass.w)
      print("total number of gray cars:",mycalss.g)
      print("others:",myclass.o)
      print("sample size:",myclsas.sample)
myobj=myclass()
myobj.check_color()
myobj.display_result()

            
