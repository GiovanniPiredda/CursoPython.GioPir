''' Desarrollar una aplicación que tenga 2 componentes cajas de texto y un
componente botón que permita calcular el porcentaje de una cantidad
colocada en el primer campo de texto.

'''

# Import the required libraries
from tkinter import *

# Create an instance of tkinter frame or window
win=Tk()

# Set the size of the tkinter window
win.geometry("700x350")

def cal_perc():
   t1=float(a.get())
   t2=float(b.get())
   percentage=t1*t2/100
   label.config(text=percentage)

# Create an Entry widget
Label(win, text="Quantity", font=('Calibri 10')).pack()
a=Entry(win, width=35)
a.pack()
Label(win, text="Enter %", font=('Calibri 10')).pack()
Label(win, text="[1-100]", font=('Calibri 10')).pack()
b=Entry(win, width=35)
b.pack()

label=Label(win, text="Percentage : ", font=('Calibri 15'))
label.pack(pady=20)

Button(win, text="Calculate Percentage", command=cal_perc).pack()

win.mainloop()