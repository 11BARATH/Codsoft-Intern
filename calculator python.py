# INTERN CALCULATOR

from tkinter import *
root = Tk()
root.title("Calculator")
input = Entry(root, width=50, borderwidth=5)
input.grid(row=0, column=0, columnspan=4, padx=15, pady=35)
current_exp = ""
def click(num):
    global current_exp
    current_exp += str(num)
    input.delete(0, END)
    input.insert(0, current_exp)
def equal():
    global current_exp
    try:
        total = str(eval(current_exp))
        input.delete(0, END)
        input.insert(0, total)
        current_exp = total
    except:
        input.delete(0, END)
        input.insert(0, "ERROR")
        current_exp = ""
def clear():
    global current_exp
    current_exp = ""
    input.delete(0, END)

button_1 = Button(root,text="1",padx=50,pady=25,command=lambda:click('1'))
button_2 = Button(root,text="2",padx=50,pady=25,command=lambda:click('2'))
button_3 = Button(root,text="3",padx=50,pady=25,command=lambda:click('3'))
button_4 = Button(root,text="4",padx=50,pady=25,command=lambda:click('4'))
button_5 = Button(root,text="5",padx=50,pady=25,command=lambda:click('5'))
button_6 = Button(root,text="6",padx=50,pady=25,command=lambda:click('6'))
button_7 = Button(root,text="7",padx=50,pady=25,command=lambda:click('7'))
button_8 = Button(root,text="8",padx=50,pady=25,command=lambda:click('8'))
button_9 = Button(root,text="9",padx=50,pady=25,command=lambda:click('9'))
button_0 = Button(root,text="0",padx=50,pady=25,command=lambda:click('0'))
button_add = Button(root,text="+",padx=48,pady=62,command=lambda:click('+'))
button_sub = Button(root,text="-",padx=49,pady=25,command=lambda:click('-'))
button_div = Button(root,text="/",padx=49,pady=25,command=lambda:click('/'))
button_mul = Button(root,text="*",padx=49,pady=25,command=lambda:click('*'))
button_mod = Button(root,text="%",padx=49,pady=25,command=lambda:click('%'))
button_equal = Button(root,text="=",padx=108,pady=25,command=equal)
button_clear = Button(root,text="AC",padx=102,pady=25,command=clear)

button_clear.grid(row=1,column=0,columnspan=2)
button_mod.grid(row=1,column=2)
button_div.grid(row=1,column=3)

button_7.grid(row=2,column=0)
button_8.grid(row=2,column=1)
button_9.grid(row=2,column=2)
button_mul.grid(row=2,column=3)

button_4.grid(row=3,column=0)
button_5.grid(row=3,column=1)
button_6.grid(row=3,column=2)
button_sub.grid(row=3,column=3)

button_1.grid(row=4,column=0)
button_2.grid(row=4,column=1)
button_3.grid(row=4,column=2)
button_add.grid(row=4,column=3,rowspan=2)

button_0.grid(row=5,column=0)
button_equal.grid(row=5,column=1,columnspan=2)

root.mainloop()




