from tkinter import *
def Bin():
    n=bin(int(e1.get()))[2:]
    res.set(n)
def Oct():
    n=oct(int(e1.get()))[2:]
    res.set(n)
def Hex():
    n=hex(int(e1.get()))[2:]
    res.set(n)
r=Tk()
res=StringVar()
l1=Label(r,text="Enter Decimal number")
e1=Entry(r)
l1.grid(row=0)
e1.grid(row=1)
l2=Label(r,text="Result:").grid(row=3)
result=Label(r, text="", textvariable=res).grid(row=3,column=1)
b = Button(r, text="Binary", command=Bin)
b.grid(row=0, column=1)
b = Button(r, text="Octal", command=Oct)
b.grid(row=1, column=1)
b = Button(r, text="Hexadecimal", command=Hex)
b.grid(row=2, column=1)
r.mainloop()
