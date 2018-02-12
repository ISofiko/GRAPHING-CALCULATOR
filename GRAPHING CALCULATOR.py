# -*- coding: utf-8 -*-
"""
Created on Sat May 14 20:58:35 2016

@author: Sofia
"""

from tkinter import*   #Import necessary libraries
from tkinter.ttk import*
import math
from tkinter import messagebox
import numpy as np

win1=Tk()   #Create first window which takes user's input


win1.title('GRAPHING CALCULATOR PROGRAM')
frame1=Frame(win1).grid(row=0, column=0)     #('Setting up the Grid')
frame2=Frame(win1).grid(row=1, column=0)     #('Function Options')
frame3=Frame(win1).grid(row=2, column=0)     #('Table of Values')


#Inputted values from entry fields are all float values, combobox is a string value and checkbutton is integer.
Xmin=DoubleVar()
Xmax=DoubleVar()
Xscl=DoubleVar()
Ymin=DoubleVar()
Ymax=DoubleVar()
Yscl=DoubleVar()

sel=StringVar()
ab=IntVar()

a_var=DoubleVar()
b_var=DoubleVar()
c_var=DoubleVar()
d_var=DoubleVar()

st_x=DoubleVar()
end_x=DoubleVar()
step=DoubleVar()


lin='f(x)=ax+b'
quad='f(x)=ax^2+bx+c'
cub='f(x)=ax^3+bx^2+cx+d'
sin='f(x)=a*sin[b(x-d)]+c'
cos='f(x)=a*cos[b(x-d)]+c'
tan='f(x)=a*tan[b(x-d)]+c'

#list of possible function choices is created
functions=[lin, quad, cub, sin, cos, tan]


#function which calculates and draws graph and outputs table of values
def funs():
    global a
    global b
    global c
    global d
    global x
    global x_range
    try:
        a=float(a_var.get())   #gets a,b,c,d values from entry fields and combobox celection
        b=float(b_var.get())
        c=float(c_var.get())
        d=float(d_var.get())
        selection=sel.get()
    except:
        messagebox.showwarning("Error", "Invalid input")   #if entries are not float or integer values, a message box lets the user know

    coords=[]
    y_list=[]
    x_range=np.linspace(float(xmin), float(xmax), 10000)

    txt=Text(win2, wrap=WORD, height=43, width=45)   #text box which shows the table of values, intercepts and max/min values
    txt.grid(row=0, column=1)
    txt.insert(0., '\n\n'+selection+'\n\nX       ,      f(x)\n\n\n')

    for x in x_range:                 #calculates f(x) depending on the function chosen
        if selection==functions[0]:
            y=(a*x)+b
        elif selection==functions[1]:
            y=(a*(x**2))+(b*x)+c
        elif selection==functions[2]:
            y=(a*(x**3))+(b*(x**2))+(c*x)+d
        elif selection==functions[3]:
            y=a*math.cos(b*(x-d))+c
        elif selection==functions[4]:
            y=a*math.sin(b*(x-d))+c
        elif selection==functions[5]:
            y=a*math.tan(b*(x-d))+c

        if int(ab.get())==1:   #absolute option for tan function
            y=abs(y)

        if y>=ymin and y<=ymax:
            coords.append((x0+(x*x_unit),y0-(y*y_unit)))
            y_list.append(y)

        elif len(coords)>1:
            canvas.create_line(coords, smooth=1, arrow=BOTH)
            coords.clear()


        if selection not in functions:
            messagebox.showwarning("Error", "Invalid function selection")



 #inserts x and f(x) for table of values, intercepts and min/max values.
        txt.insert(END, str(x)+'  ,  '+str(y)+'\n')
        if round(x,2)==0:
            txt.insert(0., '\nY-intercept: '+str(y))
        if round(y,2)==0:
            txt.insert(0., '\nX-intercept: '+str(x))


    txt.insert(0., "\nY max: "+str(max(y_list)))
    txt.insert(0., "\nY min: "+str(min(y_list)))


    if len(coords)>1:
        canvas.create_line(coords, smooth=1, arrow=BOTH)

    mainloop()



#main function, summoned by the 'submit' button
def main():
    global win2
    global xmin
    global xmax
    global xscl

    global ymin
    global ymax
    global yscl
    try:
        xmin=Xmin.get()
        xmax=Xmax.get()
        xscl=Xscl.get()

        ymin=Ymin.get()
        ymax=Ymax.get()
        yscl=Yscl.get()
    except:
        messagebox.showwarning("Error", "Invalid input")


#X and Y min always have to be negative
#X and Y max always have to be positive
#X and Y scl always have to be positive

    try:
        if xmin>=0:
            xmin=-1*xmin
        if xmax<=0:
            xmax=-1*xmax
        if xscl<=0:
            xscl=-1*xscl
        if ymin>=0:
            ymin=-1*ymin
        if ymax<=0:
            ymax=-1*ymax
        if yscl<=0:
            yscl=-1*yscl
    except:
        messagebox.showwarning("Error", "Invalid input")


    try:
        global x_unit
        global y_unit
        global canvas
        global x0
        global y0
        x_unit=900/(xmax-xmin)
        y_unit=600/(ymax-ymin)
        win2=Tk()    #new graph window is created
        win2.title("GRAPH AND TABLE OF VALUES")
        canvas=Canvas(win2, width=1000, height=700, bg='light yellow')   #graph is drawn on the canvas
        canvas.grid(row=0, column=0)

        y0=650+(y_unit*ymin)   #ymin is negative
        x0=50-(x_unit*xmin)   #this brings the (0,0) coordinates from top left to the origin of the graph
        canvas.create_line(50, y0, 950, y0, fill='blue', arrow=BOTH) #x axis is drawn
        canvas.create_line(x0, 50, x0, 650, fill='blue', arrow=BOTH)  #y axis is drawn

        for i in range(int(xmin*x_unit), int(xmax*x_unit)+int(xscl*x_unit), int(xscl*x_unit)):
            canvas.create_text(x0+i, y0+10, text=str(round(i/x_unit, 3)), fill='dark blue')   #x axis is labeled, rounded to 3 decimal places

        for i in range(0, int(ymax*y_unit)-int(ymin*y_unit) +int(yscl*y_unit), int(yscl*y_unit)):
            canvas.create_text(70-int(x_unit*xmin), 650-i, text=str(round(i/y_unit+ymin, 3)), fill='dark blue')   #y axis is labeled, rounded to 3 decimal places

    except ValueError:
        messagebox.showwarning("Error", "Invalid input")

    funs()   #function program is called



            #Setting up the grid
sL1=ttk.Style()
sL1.configure('Kim.TButton', foreground='maroon')

#all entry fields and labels are created, also combobox and checkbutton
blank1=Label(frame1, text='   ').grid(column=0, row=0, columnspan=8)

labX1=Label(frame1, text='Xmin: ', style='Kim.TButton').grid(column=1, row=1)
entX1=Entry(frame1, width=10, textvar=Xmin).grid(column=2, row=1)

labX2=Label(frame1, text='Xmax: ', style='Kim.TButton').grid(column=3, row=1)
entX2=Entry(frame1, width=10, textvar=Xmax).grid(column=4, row=1)

labX3=Label(frame1, text='Xscl: ', style='Kim.TButton').grid(column=5, row=1)
entX3=Entry(frame1, width=10, textvar=Xscl).grid(column=6, row=1)


labY1=Label(frame1, text='Ymin: ', style='Kim.TButton').grid(column=1, row=2)
entY1=Entry(frame1, width=10, textvar=Ymin).grid(column=2, row=2)

labY2=Label(frame1, text='Ymax: ', style='Kim.TButton').grid(column=3, row=2)
entY2=Entry(frame1, width=10, textvar=Ymax).grid(column=4, row=2)

labY3=Label(frame1, text='Yscl: ', style='Kim.TButton').grid(column=5, row=2)
entY3=Entry(frame1, width=10, textvar=Yscl).grid(column=6, row=2)

blank2=Label(frame1, text='   ').grid(row=3, column=0, columnspan=8)


            #Function options
global entA
global entB
global entC
global entD
sel_fun=Combobox(frame2, textvariable=sel, values=functions).grid(column=0, row=4, columnspan=8)
sel.set(functions[0])

sCh=ttk.Style()
sCh.configure("Red.TCheckbutton", foreground="orange")
absolute=Checkbutton(frame2, text='Absolute', variable=ab, style='Red.TCheckbutton').grid(column=0, row=5, columnspan=8)



blank3=Label(frame2, text='   ').grid(row=6, column=0, columnspan=8)

labA=Label(frame2, text=' '*10+'a', width=10).grid(column=0, row=7)
entA=Entry(frame2, width=10, textvar=a_var).grid(column=1, row=7)
labB=Label(frame2, text='b').grid(column=2, row=7)
entB=Entry(frame2, width=10, textvar=b_var).grid(column=3, row=7)
labC=Label(frame2, text='c').grid(column=4, row=7)
entC=Entry(frame2, width=10, textvar=c_var).grid(column=5, row=7)
labD=Label(frame2, text='d').grid(column=6, row=7)
entD=Entry(frame2, width=10, textvar=d_var).grid(column=7, row=7)


blank4=Label(frame2, text='   ').grid(row=8, column=0, columnspan=8)

sB=ttk.Style()
sB.configure('green/black.TButton', foreground='green', background='red', relief=RAISED)
submit=Button(frame3, text='Submit', command=main, style='green/black.TButton')
submit.grid(column=0, row=9, columnspan=8)

blank5=Label(frame2, text='  ').grid(row=10, column=0, columnspan=8)
blank6=Label(win1, text='  ', width=2).grid(row=0, column=8, rowspan=8)


mainloop()