from tkinter import *

f_num = 0
expression = ""
root = Tk()
root.title("SImple calculator")
e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def button_clear():
    e.delete(0, END)
    global f_num
    global expression
    f_num = 0
    expression = ""


# creating a button

button1 = Button(root, text="1", padx=40, pady=40, command=lambda: button_click(1))
button2 = Button(root, text="2", padx=40, pady=40, command=lambda: button_click(2))
button3 = Button(root, text="3", padx=40, pady=40, command=lambda: button_click(3))
button4 = Button(root, text="4", padx=40, pady=40, command=lambda: button_click(4))
button5 = Button(root, text="5", padx=40, pady=40, command=lambda: button_click(5))
button6 = Button(root, text="6", padx=40, pady=40, command=lambda: button_click(6))
button7 = Button(root, text="7", padx=40, pady=40, command=lambda: button_click(7))
button8 = Button(root, text="8", padx=40, pady=40, command=lambda: button_click(8))
button9 = Button(root, text="9", padx=40, pady=40, command=lambda: button_click(9))
button0 = Button(root, text="0", padx=40, pady=40, command=lambda: button_click(0))


def button_calc(exp):
    first_num = e.get()
    global f_num
    global expression
    expression = exp
    f_num = int(first_num)
    e.delete(0, END)


buttonAdd = Button(root, text="+", padx=39, pady=40, command=lambda: button_calc("+"))


def button_equal():
    s_num = e.get()
    e.delete(0, END)
    if expression == "+":
        e.insert(0, int(f_num) + int(s_num))
    elif expression == "-":
        e.insert(0, int(f_num) - int(s_num))
    elif expression == "*":
        e.insert(0, int(f_num) * int(s_num))
    elif expression == "/":
        e.insert(0, int(f_num) / int(s_num))
    else:
        e.insert(0, int(s_num))


buttonEqual = Button(root, text="=", padx=91, pady=40, command=lambda: button_equal())

buttonClear = Button(root, text="clear", padx=79, pady=40, command=button_clear)

buttonSub = Button(root, text="-", padx=39, pady=40, command=lambda: button_calc("-"))

buttonMul = Button(root, text="*", padx=39, pady=40, command=lambda: button_calc("*"))

buttonDiv = Button(root, text="/", padx=39, pady=40, command=lambda: button_calc("/"))
# buttonClear = Button(root, text="clear", padx=79, pady=40, command=lambda: button_click()

# Put the buttons on the Screen
button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

button0.grid(row=4, column=0)
buttonClear.grid(row=4, column=1, columnspan=2)
buttonAdd.grid(row=5, column=0)
buttonSub.grid(row=5, column=1)
buttonMul.grid(row=5, column=2)
buttonDiv.grid(row=6, column=0)
buttonEqual.grid(row=6, column=1, columnspan=2)
# button1.grid(row=,column=)

root.mainloop()
