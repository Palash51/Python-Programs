from tkinter import *
# if you are working under Python 3, comment the previous line and comment out the following line
#from tkinter import *

root = Tk() #blank window

#theLable = Label(root, text="Hello Tkinter!, palash patidar")
#theLable.pack()

'''topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

button1 = Button(topFrame, text="Button 1", fg="red")
button2 = Button(topFrame, text="Button 2", fg="blue")
button3 = Button(topFrame, text="Button 3", fg="green")
button4 = Button(bottomFrame, text="Button 4", fg="purple")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)
'''

one = Label(root, text="One", bg="red", fg="white")
one.pack()
two = Label(root, text="two", bg="green", fg="black")
two.pack(fill=X)
three = Label(root, text="three", bg="blue", fg="white")
three.pack(side=LEFT, fill=Y)


root.mainloop()
