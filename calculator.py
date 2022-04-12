from glob import glob
from tkinter import*

from setuptools import Command
calcbody=Tk()
calcbody.title("calculator")
#calcbody.geometry("500x600")

def clickbtn(num):
    current=e.get()#nolasa skaitli
    e.delete(0,END)#nodzēš
    newNumber=str(current)+str(num)
    e.insert(0,newNumber)# ievieto disp
    return 0

def cmdbtn(command):
    global num1#iegaume sk un darb
    global mathOp #mat operators
    mathOp=command # darbibas
    num1=int(e.get())
    e.delete(0,END)
    return 0
e=Entry(calcbody,width=20,font=("Arial",26),bg="black",fg="lightgreen")
poga0=Button(calcbody,text="0",bg="black",fg="lightgreen",padx="40",pady="20",command=lambda:clickbtn(0))
poga1=Button(calcbody,text="1",bg="black",fg="lightgreen",padx="40",pady="20",command=lambda:clickbtn(1))
poga2=Button(calcbody,text="2",bg="black",fg="lightgreen",padx="40",pady="20",command=lambda:clickbtn(2))
poga3=Button(calcbody,text="3",bg="black",fg="lightgreen",padx="40",pady="20",command=lambda:clickbtn(3))
poga4=Button(calcbody,text="4",bg="black",fg="lightgreen",padx="40",pady="20",command=lambda:clickbtn(4))
poga5=Button(calcbody,text="5",bg="black",fg="lightgreen",padx="40",pady="20",command=lambda:clickbtn(5))
poga6=Button(calcbody,text="6",bg="black",fg="lightgreen",padx="40",pady="20",command=lambda:clickbtn(6))
poga7=Button(calcbody,text="7",bg="black",fg="lightgreen",padx="40",pady="20",command=lambda:clickbtn(7))
poga8=Button(calcbody,text="8",bg="black",fg="lightgreen",padx="40",pady="20",command=lambda:clickbtn(8))
poga9=Button(calcbody,text="9",bg="black",fg="lightgreen",padx="40",pady="20",command=lambda:clickbtn(9))
pogasum=Button(calcbody,text="=",bg="black",fg="lightgreen",padx="40",pady="20")
pogac=Button(calcbody,text="C",bg="black",fg="lightgreen",padx="40",pady="20")
pogaminus=Button(calcbody,text="-",bg="black",fg="lightgreen",padx="40",pady="20",command=lambda:cmdbtn("-"))
pogadal=Button(calcbody,text="/",bg="black",fg="lightgreen",padx="40",pady="20",command=lambda:cmdbtn("/"))
pogareiz=Button(calcbody,text="*",bg="black",fg="lightgreen",padx="40",pady="20",command=lambda:cmdbtn("*"))
pogaplus=Button(calcbody,text="+",bg="black",fg="lightgreen",padx="40",pady="20",command=lambda:cmdbtn("+"))

e.grid(row=0,column=0,columnspan=5)
pogaminus.grid(row=4,column=4)
pogadal.grid(row=3,column=4)
pogareiz.grid(row=2,column=4)
pogaplus.grid(row=1,column=4)
pogac.grid(row=4,column=0)
pogasum.grid(row=4,column=2)
poga7.grid(row=1,column=0)
poga8.grid(row=1,column=1)
poga9.grid(row=1,column=2) 
poga4.grid(row=2,column=0)
poga5.grid(row=2,column=1)
poga6.grid(row=2,column=2)
poga1.grid(row=3,column=0)
poga2.grid(row=3,column=1)
poga3.grid(row=3,column=2)
poga0.grid(row=4,column=1)
calcbody.mainloop()