from tkinter import*

root = Tk()

#creating a label widget
myLabel1= Label(root,text="helloworld!")
myLabel2=Label(root,text="My name is SWETHA")
myLabel3= Label(root,text="                  ")
#showing it onto the screen
myLabel1.grid(row=0,column=0)
myLabel2.grid(row=1,column=5)
myLabel3.grid(row=1,column=1)




root.mainloop()