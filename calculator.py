from cmath import sqrt
from glob import glob
from sqlite3 import SQLITE_TRANSACTION
from tkinter import*
from tkinter.tix import COLUMN
from turtle import clear
import tkinter.messagebox

from setuptools import Command
calcbody=Tk()
calcbody.title("matrix style calculator")
#calcbody.geometry("600x700")


calcbody.configure(background = 'black')
calcbody.resizable(width=False, height=False)
#nosledz kalkulatoru noteiktaja loga

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
    num1=float(e.get())
    e.delete(0,END)
    return 0

def equals():
    global num2
    num2=float(e.get())
    result=0
    if mathOp=="+":
        result=num1+num2
    elif mathOp=="-":
        result=num1-num2
    elif mathOp=="*":
        result=num1*num2
    elif mathOp=="/":
        result=num1/num2
    else:
        result=0
    e.delete(0,END)
    e.insert(0,str(result))
    return 0

def Clear():
    e.delete(0,END)
    num1=0
    mathOp=""
    return 0 
    
def sq_rt():
    global operator
    global num1
    num1=(float(e.get()))
    num1=sqrt(num1)
    e.delete(0,END)
    e.insert(0,num1)
    return 0


def perc():
    global num2
    num2=float(e.get())
    result=0
    if mathOp=="+":
        result=num1+(num2*num1*0.01)
    elif mathOp=="-":
        result=num1-(num2*num1*0.01)
    elif mathOp=="*":
        result=num2*num1*0.01
    elif mathOp=="/":
        result=num1/(num2*num1*0.01)   
    else:
        result=0
    e.delete(0,END)
    e.insert(0,str(result))
    return 0
#veic procentu darbibu(procents ir otrais skaitlis)

def Dot():
    pos = len(e.get())
    e.insert(pos, '.')


e=Entry(calcbody,width=25,font=("Arial",25),bg="black",fg="lightgreen")
poga0=Button(calcbody,font=("Arial",11),text="0",bg="black",fg="lightgreen",padx="40",pady="10",command=lambda:clickbtn(0))
poga1=Button(calcbody,font=("Arial",11),text="1",bg="black",fg="lightgreen",padx="40",pady="10",command=lambda:clickbtn(1))
poga2=Button(calcbody,font=("Arial",11),text="2",bg="black",fg="lightgreen",padx="40",pady="10",command=lambda:clickbtn(2))
poga3=Button(calcbody,font=("Arial",11),text="3",bg="black",fg="lightgreen",padx="40",pady="10",command=lambda:clickbtn(3))
poga4=Button(calcbody,font=("Arial",11),text="4",bg="black",fg="lightgreen",padx="40",pady="10",command=lambda:clickbtn(4))
poga5=Button(calcbody,font=("Arial",11),text="5",bg="black",fg="lightgreen",padx="40",pady="10",command=lambda:clickbtn(5))
poga6=Button(calcbody,font=("Arial",11),text="6",bg="black",fg="lightgreen",padx="40",pady="10",command=lambda:clickbtn(6))
poga7=Button(calcbody,font=("Arial",11),text="7",bg="black",fg="lightgreen",padx="40",pady="10",command=lambda:clickbtn(7))
poga8=Button(calcbody,font=("Arial",11),text="8",bg="black",fg="lightgreen",padx="40",pady="10",command=lambda:clickbtn(8))
poga9=Button(calcbody,font=("Arial",11),text="9",bg="black",fg="lightgreen",padx="40",pady="10",command=lambda:clickbtn(9))
pogaminus=Button(calcbody,font=("Arial",11),text="-",bg="black",fg="lightgreen",padx="40",pady="10",command=lambda:cmdbtn("-"))
pogadal=Button(calcbody,font=("Arial",11),text="/",bg="black",fg="lightgreen",padx="40",pady="10",command=lambda:cmdbtn("/"))
pogareiz=Button(calcbody,font=("Arial",11),text="*",bg="black",fg="lightgreen",padx="40",pady="10",command=lambda:cmdbtn("*"))
pogaplus=Button(calcbody,font=("Arial",11),text="+",bg="black",fg="lightgreen",padx="40",pady="10",command=lambda:cmdbtn("+"))
pogasum=Button(calcbody,font=("Arial",11),height=4,text="=",bg="black",fg="lightgreen",padx="40",pady="10",command=equals)
pogac=Button(calcbody,font=("Arial",11),text="C",bg="black",fg="lightgreen",padx="40",pady="10",command=Clear)
pogasqrt=Button(calcbody,font=("Arial",11),text="√",bg="black",fg="lightgreen",padx="40",pady="10",command=sq_rt)
pogaperc=Button(calcbody,font=("Arial",11),text="%",bg="black",fg="lightgreen",padx="40",pady="10",command=perc)
pogadot=Button(calcbody,font=("Arial",11),text=".",bg="black",fg="lightgreen",padx="40",pady="10",command=Dot)

pogaperc.grid(row=4,column=2)
pogasqrt.grid(row=1,column=5)
pogadot.grid(row=2,column=5)
e.grid(row=0,column=0,columnspan=7)
pogaminus.grid(row=4,column=3,columnspan=2)
pogadal.grid(row=3,column=4)
pogareiz.grid(row=2,column=4)
pogaplus.grid(row=1,column=4)
pogac.grid(row=4,column=0)
pogasum.grid(row=3,column=5,rowspan=2)
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


