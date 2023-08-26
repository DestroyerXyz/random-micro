from tkinter import *
import math

def num(e):
    global r,opr,g
    x = e.widget.message
    t1.insert("insert",x)
    r = str(t1.get(1.0,END))

def posneg(e):
    global r,opr,g
    if(float(r) >= 0):
        r = "-" + r
        t1.delete(1.0,END)
        t1.insert("insert",r)
    else:
        r = r.replace("-", "")
        t1.delete(1.0,END)
        t1.insert("insert",r)

def CE(e):
    global r,opr,g
    t1.delete(1.0,END)
    r = "0"

def C(e):
    global r,opr,g
    t1.delete(1.0,END)
    r = "0"
    g = "0"

def back(e):
    global r,opr,g
    h = "1."
    j = str(len(t1.get(1.0, END)) - 2)
    k = h + j
    t1.delete(float(k), END)
    r = str(t1.get(1.0,END))

def equalto(e):
    global r,opr,g
    if(opr == "+"):
        r = str(float(g) + float(r))
        t1.delete(1.0,END)
        t1.insert("insert", r)
        opr = ""
    elif(opr == "-"):
        r = str(float(g) - float(r))
        t1.delete(1.0,END)
        t1.insert("insert",r)
        opr = ""
    elif(opr == "/"):
        r = str(float(g) / float(r))
        t1.delete(1.0,END)
        t1.insert("insert", r)
        opr = ""
    elif(opr == "x"):
        r = str(float(g) * float(r))
        t1.delete(1.0,END)
        t1.insert("insert",r)
        opr = ""
    equals_to_clicked = True
        
def plus(e):
    global r,opr,g
    if(opr == ""):
        g = str(t1.get(1.0,END))
        t1.delete(1.0,END)
        opr = e.widget.message

def minus(e):
    global r,opr,g
    if(opr == ""):
        g = str(t1.get(1.0,END))
        t1.delete(1.0,END)
        opr = e.widget.message

def divide(e):
    global r,opr,g
    if(opr == ""):
        g = str(t1.get(1.0,END))
        t1.delete(1.0,END)
        opr = e.widget.message

def multiply(e):
    global r,opr,g
    if(opr == ""):
        g = str(t1.get(1.0,END))
        t1.delete(1.0,END)
        opr = e.widget.message

def percent(e):
    global r,opr,g
    if(opr != ""):
        r = str(float(float(r) / 100 * float(g)))
        t1.delete(1.0,END)
        t1.insert("insert", r)

def sqrt(e):
    global r,opr,g
    r = str(t1.get(1.0,END))
    r = str(math.sqrt(float(r)))
    t1.delete(1.0,END)
    t1.insert("insert", r)

def square(e):
    global r,opr,g
    r = str(float(r) * float(r))
    t1.delete(1.0,END)
    t1.insert("insert", r)

def onex(e):
    global r,opr,g
    r = str(1 / float(r))
    t1.delete(1.0,END)
    t1.insert("insert", r)


a1 = Tk()
a1.title("Calculator")
a1.geometry("252x430")
xx = 0
yy = 0
opr = ""
equals_to_clicked = False

t1 = Text(a1)
t1.pack()
t1.place(x = 10, y = 10,height = 50, width = 230)

b1 = Button(a1, text = "%")
b2 = Button(a1, text = "CE")
b3 = Button(a1, text = "C")
b1.pack()
b2.pack()
b3.pack()
b1.place(x = 10, y = 70,height = 50, width = 50)
b2.place(x = 70, y = 70,height = 50, width = 50)
b3.place(x = 130, y = 70,height = 50, width = 50)
b1.bind("<Button-1>",percent)
b2.bind("<Button-1>",CE)
b3.bind("<Button-1>",C)

b4 = Button(a1, text = "1/x")
b5 = Button(a1, text = "x²")
b6 = Button(a1, text = "2√x")
b4.pack()
b5.pack()
b6.pack()
b4.place(x = 10, y = 130,height = 50, width = 50)
b5.place(x = 70, y = 130,height = 50, width = 50)
b6.place(x = 130, y = 130,height = 50, width = 50)
b4.bind("<Button-1>",onex)
b5.bind("<Button-1>",square)
b6.bind("<Button-1>",sqrt)

for i in range(3):
    b7 = Button(a1, text = i + 7)
    b7.pack()
    b7.place(x = 10 + xx, y = 190,height = 50, width = 50)
    b7.message = i + 7
    b7.bind("<Button-1>",num)
    xx += 60

xx = 0

for i in range(3):
    b8 = Button(a1, text = i + 4)
    b8.pack()
    b8.place(x = 10 + xx, y = 250, height = 50, width = 50)
    b8.message = i + 4
    b8.bind("<Button-1>",num)
    xx += 60

xx = 0

for i in range(3):
    b9 = Button(a1, text = i + 1)
    b9.pack()
    b9.place(x = 10 + xx, y = 310, height = 50, width = 50)
    b9.message = i + 1
    b9.bind("<Button-1>",num)
    xx += 60

d = "-"
b10 = Button(a1, text = "+/-")
b11 = Button(a1, text = "0")
b12 = Button(a1, text = ".")
b10.pack()
b11.pack()
b12.pack()
b10.place(x = 10, y = 370, height = 50, width = 50)
b11.place(x = 70, y = 370, height = 50, width = 50)
b12.place(x = 130, y = 370, height = 50, width = 50)
b10.message = d
b11.message = 0
b12.message = "."
b10.bind("<Button-1>",posneg)
b11.bind("<Button-1>",num)
# b12.bind("<Button-1>",point)

b13 = Button(a1, text = "←")
b14 = Button(a1, text = "÷")
b15 = Button(a1, text = "x")
b16 = Button(a1, text = "-")
b17 = Button(a1, text = "+")
b18 = Button(a1, text = "=", bg = "orange")
b13.pack()
b14.pack()
b15.pack()
b16.pack()
b17.pack()
b18.pack()
b13.place(x = 190, y = 70, height = 50, width = 50)
b14.place(x = 190, y = 130, height = 50, width = 50)
b15.place(x = 190, y = 190, height = 50, width = 50)
b16.place(x = 190, y = 250, height = 50, width = 50)
b17.place(x = 190, y = 310, height = 50, width = 50)
b18.place(x = 190, y = 370, height = 50, width = 50)
b14.message = "/"
b15.message = "x"
b16.message = "-"
b17.message = "+"
b18.message = "="
b13.bind("<Button-1>",back)
b14.bind("<Button-1>",divide)
b15.bind("<Button-1>",multiply)
b16.bind("<Button-1>",minus)
b17.bind("<Button-1>",plus)
b18.bind("<Button-1>",equalto)

a1.mainloop()