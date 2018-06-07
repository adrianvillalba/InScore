# -*- coding: utf-8 -*-
#Importing Tkinter GUI module
import Tkinter
from Tkinter import *
import tkMessageBox
from Tkinter import Label

#Defining the function to calculate the insulitis score:
def Insulitis_Score():
    Islet_0 = float(caja1.get())
    Islet_1 = float(caja2.get())
    Islet_2 = float(caja3.get())
    Islet_3 = float(caja4.get())
    Islet_4 = float(caja5.get())
    a = Islet_0*0 
    b = Islet_1*1
    c = Islet_2*2
    d = Islet_3*3
    e = Islet_4*4
    total = Islet_0 + Islet_1 + Islet_2 + Islet_3 + Islet_4
    Result = (a+b+c+d+e)/total
    Islet0_percentage = Islet_0/total * 100
    Islet1_percentage = Islet_1/total * 100
    Islet2_percentage = Islet_2/total * 100
    Islet3_percentage = Islet_3/total * 100
    Islet4_percentage = Islet_4/total * 100
    tkMessageBox.showinfo("Result", "The Insulitis Score value is {0}.".format(str(Result)))
    
    if total < 40:
        tkMessageBox.showinfo("Islet number","You scored {0} islets, at least 40 islets are needed to have reliable results.".format(str(total)))
    
    cajaM.delete(0, END)
    caja1.delete(0, END)
    caja2.delete(0, END)
    caja3.delete(0, END)
    caja4.delete(0, END)
    caja5.delete(0, END)

#Method to create the GUI:
gui = Tk()
gui.title("Insulitis Score Calculator")
gui.geometry("400x500+400+100")
etiqueta = Label(gui, text='Welcome to the Insulitis Score Calculator!')
etiqueta.pack(expand=YES, fill=BOTH)

#Design of the label:
varX = StringVar()
varX.set("Enter the code for your specimen:")
labelY = Label(gui,textvariable=varX,height = 2)
labelY.pack()

numeroN=StringVar()
cajaM=Entry(gui,bd=4,textvariable=numeroN)
cajaM.pack()

varZ = StringVar()
varZ.set("")
labelZ = Label(gui,textvariable=varZ,height = 2)
labelZ.pack()

var0 = StringVar()
var0.set("Enter the number of islets with score 0:")
label1 = Label(gui,textvariable=var0,height = 2)
label1.pack()

numero0=StringVar()
caja1=Entry(gui,bd=4,textvariable=numero0)
caja1.pack()

var1 = StringVar()
var1.set("Enter the number of islets with score 1:")
label2 = Label(gui,textvariable=var1,height = 2)
label2.pack()

numero1=StringVar()
caja2=Entry(gui,bd=4,textvariable=numero1)
caja2.pack()

var2 = StringVar()
var2.set("Enter the number of islets with score 2:")
label3 = Label(gui,textvariable=var2,height = 2)
label3.pack()

numero2=StringVar()
caja3=Entry(gui,bd=4,textvariable=numero2)
caja3.pack()

var3 = StringVar()
var3.set("Enter the number of islets with score 3:")
label4 = Label(gui,textvariable=var3,height = 2)
label4.pack()

numero3=StringVar()
caja4=Entry(gui,bd=4,textvariable=numero3)
caja4.pack()

var4 = StringVar()
var4.set("Enter the number of islets with score 4:")
label5 = Label(gui,textvariable=var4,height = 2)
label5.pack()

numero4=StringVar()
caja5=Entry(gui,bd=4,textvariable=numero4)
caja5.pack()


#Design of the button to Calculate the insulitis score:
boton1 = Button(gui, text = "CALCULATE", command = Insulitis_Score, width=15)
boton1.pack()

#Design of the credits:
etiqueta2=Label(gui, text="Credits: Adrián Villalba, adri.vife@gmail.com")
etiqueta2.pack(expand=YES, fill=BOTH)

#Running the GUI:
gui.mainloop()
etiqueta.mainloop()
etiqueta2.mainloop()