from tkinter import *

window=Tk()
window.geometry("250x150")
window.title("Calculator")
window.configure(bg="grey")
disp=StringVar()
display=Entry(window,textvariable=disp).grid(columnspan=4, ipadx=70)

button7=Button(window,text=7)
button8=Button(window,text=8)
button9=Button(window,text=9)
buttonPLUS=Button(window,text="+")
button4=Button(window,text=4)
button5=Button(window,text=5)
button6=Button(window,text=6)
buttonMINUS=Button(window,text="-")
button1=Button(window,text=1)
button2=Button(window,text=2)
button3=Button(window,text=3)
buttonMULT=Button(window,text="*")
buttonCLR=Button(window,text="CLR")
button0=Button(window,text=0)
buttonEQU=Button(window,text="=")
buttonDIV=Button(window,text="/")

button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)
buttonPLUS.grid(row=1,column=3)
button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)
buttonMINUS.grid(row=2,column=3)
button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)
buttonMULT.grid(row=3,column=3)
buttonCLR.grid(row=4,column=0)
button0.grid(row=4,column=1)
buttonEQU.grid(row=4,column=2)
buttonDIV.grid(row=4,column=3)
window.mainloop()