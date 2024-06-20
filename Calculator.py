from tkinter import *

window=Tk()
window.geometry("320x400")
window.title("Calculator")
window.configure(bg="grey")

expression=""
def displ(value):
    global expression
    expression=expression+str(value)
    disp.set(expression)


disp = StringVar()
display=Entry(window,textvariable=disp,state=DISABLED).grid(columnspan=4, ipadx=97, ipady=20)

button7=Button(window,text=7,width=10,height=5, command=lambda: displ(7)).grid(row=1,column=0)
button8=Button(window,text=8,width=10,height=5, command=lambda: displ(8)).grid(row=1,column=1)
button9=Button(window,text=9,width=10,height=5, command=lambda: displ(9)).grid(row=1,column=2)
buttonPLUS=Button(window,text="+",width=10,height=5, command=lambda: displ("+")).grid(row=1,column=3)
button4=Button(window,text=4,width=10,height=5, command=lambda: displ(4)).grid(row=2,column=0)
button5=Button(window,text=5,width=10,height=5, command=lambda: displ(5)).grid(row=2,column=1)
button6=Button(window,text=6,width=10,height=5, command=lambda: displ(6)).grid(row=2,column=2)
buttonMINUS=Button(window,text="-",width=10,height=5, command=lambda: displ("-")).grid(row=2,column=3)
button1=Button(window,text=1,width=10,height=5, command=lambda: displ(1)).grid(row=3,column=0)
button2=Button(window,text=2,width=10,height=5, command=lambda: displ(2)).grid(row=3,column=1)
button3=Button(window,text=3,width=10,height=5, command=lambda: displ(3)).grid(row=3,column=2)
buttonMULT=Button(window,text="*",width=10,height=5, command=lambda: displ("*")).grid(row=3,column=3)
buttonCLR=Button(window,text="CLR",width=10,height=5, command=clear).grid(row=4,column=0)
button0=Button(window,text=0,width=10,height=5, command=lambda: displ(0)).grid(row=4,column=1)
buttonEQU=Button(window,text="=",width=10,height=5, command=equ).grid(row=4,column=2)
buttonDIV=Button(window,text="/",width=10,height=5, command=lambda: displ("/")).grid(row=4,column=3)


window.mainloop()