#Creating a GU Calculator App using python and tkinter.
#importing tkinter module

from tkinter import *

#Function to calculate 
def calculate():
    display["text"] = eval(display["text"])

#function to add numbers to the display

def addNumbers(x):
    display["text"] += x
#Clear Function
def clear():
    display["text"] = ""
#Creating GUI

root = Tk()
root.title("Calculator")
#Display
display = Label(root, width=30, height=3)
display.grid(row=0,column=0, columnspan=4)

#Creating buttons
btn_add = Button(root, text="+", width=2, height=2, command=lambda:addNumbers("+"))
btn_add.grid(row= 6,column=3)

btn_sub = Button(root, text= "-", width=2, height=2, command=lambda:addNumbers("-"))
btn_sub.grid(row=5, column=3)

btn_mul = Button(root, text= "*", width=2, height=2, command=lambda:addNumbers("*"))
btn_mul.grid(row=4, column= 3)

btn_div = Button(root, text="/",width=2, height=2, command=lambda:addNumbers("/"))
btn_div.grid(row=3, column=3)

btn_clear = Button(root, text = " C ", width=10, height=2, fg= "red", command=lambda:clear())
btn_clear.grid(row=3, column=0, columnspan=2)

btn_mod = Button(root, text="%", width=2, height=2, command=lambda:addNumbers("%"))
btn_mod.grid(row=3,column=2)

#Creating numbers
btn1 = Button(root,text= "1", width= 2, height= 2, command=lambda:addNumbers("1"))
btn1.grid(row=4, column=0)

btn2 = Button(root,text= "2", width= 2, height= 2, command=lambda:addNumbers("2"))
btn2.grid(row=4,column=1)

btn3 = Button(root,text= "3", width= 2, height= 2, command=lambda:addNumbers("3"))
btn3.grid(row=4,column=2)

btn4 = Button(root,text= "4", width= 2, height= 2, command=lambda:addNumbers("4"))
btn4.grid(row=5,column=0)

btn5 = Button(root,text= "5", width= 2, height= 2, command=lambda:addNumbers("5"))
btn5.grid(row=5,column=1)

btn6 = Button(root,text= "6", width=2, height= 2, command=lambda:addNumbers("6"))
btn6.grid(row=5,column=2)

btn7 = Button(root,text= "7", width= 2, height= 2, command=lambda:addNumbers("7"))
btn7.grid(row=6,column=0)

btn8 = Button(root,text= "8", width= 2, height= 2, command=lambda:addNumbers("8"))
btn8.grid(row=6,column=1)

btn9 = Button(root,text= "9", width= 2, height= 2, command=lambda:addNumbers("9"))
btn9.grid(row=6,column=2)

btn_dot = Button(root,text= ".", width= 2, height= 2, command=lambda:addNumbers("."))
btn_dot.grid(row=7,column=0)

btn0 = Button(root,text= "0", width= 2, height= 2, command=lambda:addNumbers("0"))
btn0.grid(row=7,column=1)

btn_calc = Button(root,text= " = ", width= 4, height= 2, command=lambda:calculate())
btn_calc.grid(row=7,column=2, columnspan=2)


#tkinter main loop
root.mainloop()