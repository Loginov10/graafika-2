from math import*
from tkinter import *
import random



def valgusfoor():
    tahvel=Tk()
    tahvel.title("Tahvel")
    tahv=Canvas(tahvel,width=600,height=600,background="grey")

    tahv.create_rectangle(100,570,  500,580, fill="black")
    tahv.create_rectangle(290,560,  300,320, fill="black")
    red_light=tahv.create_rectangle(250,240,  340,310,outline="Black", fill="grey")
    yellow_light=tahv.create_rectangle(250,160,  340,230,outline="Black", fill="grey")
    green_light=tahv.create_rectangle(250,80,  340,150,outline="Black", fill="grey")
    tahv.grid()

    def switch():
        if var.get() == 1:
            tahv.itemconfig(red_light, fill='red')
            tahv.itemconfig(yellow_light, fill='black')
            tahv.itemconfig(green_light, fill='black')
        elif var.get() == 2:
            tahv.itemconfig(red_light, fill='black')
            tahv.itemconfig(yellow_light, fill='yellow')
            tahv.itemconfig(green_light, fill='black')
        else:
            tahv.itemconfig(red_light, fill='black')
            tahv.itemconfig(yellow_light, fill='black')
            tahv.itemconfig(green_light, fill='green')
    return switch
    



def board():
    tahvel=Tk()
    tahvel.title("Tahvel")
    tahvel=Canvas(tahvel,width=600,height=600)
    color = 'white'
 
    for y in range(8):

        for x in range(8):
            x1 = x*70
            y1 = y*70
            x2 = x1 + 70
            y2 = y1 + 70
            tahvel.create_rectangle((x1, y1, x2, y2), fill=color)
            if color == 'white':
                color = 'black'
            else:    
                color = 'white'

        if color == 'white':
            color = 'black'
        else:    
             color = 'white'
        tahvel.grid()
def muster():
    aa=Tk()
    aa.title("Tahvel")
    aa=Canvas(aa,width=600,height=600,background="white")
    x0=0
    y0=0
    x1=600
    y1=600
    a=300
    r=(a**2+a**2)**(1/2)
    p=(a-r)
    for i in range(12):
        x1-=p
        y1-=p
        x0+=p
        y0+=p
        aa.create_rectangle(x0,y0,x1,y1,width=1,outline="blue",fill="red")
        aa.create_oval(x0,y0,y1,x1,width=1,outline="blue",fill="yellow")
        p=r-a
        r=r-p
        a=((r)*sqrt(2))/2

    aa.grid()
def ringad():
    colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet","purple","lightblue","pink","cyan","magenta"]
    tahvel=Tk()
    tahvel.title("Tahvel")
    tahvel=Canvas(tahvel,width=600,height=600,background="white")
    radius = 300
    center = 300,300
    k=30
    for i in range(k):
        radius-=10
        tahvel.create_oval(center[0] - radius, center[1] - radius,
                        center[0] + radius, center[1] + radius,fill=random.choice(colors))


    tahvel.grid()

def eesti():
    nupp.configure()
    tahvel=Tk()
    tahvel.title("Tahvel")
    tahvel=Canvas(tahvel,width=200,height=200)
    tahvel.create_rectangle(190,100,  10,25, fill="blue")
    tahvel.create_rectangle(190,100,  10,60, fill="black")
    tahvel.create_rectangle(190,100,  10,135, fill="white")
    tahvel.grid()
    

def baham():
    nupp2.configure()
    tahvel=Tk()
    tahvel.title("Tahvel")
    tahvel=Canvas(tahvel,width=200,height=200)
    tahvel.create_rectangle(190,100,  10,25, fill="#67c1cf")
    tahvel.create_rectangle(190,100,  10,60, fill="yellow")
    tahvel.create_rectangle(190,100,  10,135, fill="#67c1cf")
    tahvel.create_polygon(190,25,  190,135,  90,80, fill="black")
    tahvel.grid()

tekst="Aken"
aken=Tk()
aken.geometry("300x200")  #разрешение экрана
aken.title(tekst)          #заголовок

nupp=Radiobutton(aken,text="Eesti lipp",command=eesti)

nupp2=Radiobutton(aken,text="Bahama saarte lipp",command=baham)

nupp3=Radiobutton(aken,text="Muster",command=muster)

nupp4=Radiobutton(aken,text="Mälu", command=board)

nupp5=Radiobutton(aken,text="Ringad",command=ringad)

nupp6=Radiobutton(aken,text="Valgusfoor",command=valgusfoor)

var = IntVar()
radio_red = Radiobutton(aken, text="Red", bg="red",variable=var,value=1,command=valgusfoor)

radio_yellow = Radiobutton(aken, text="yellow", bg="yellow",variable=var,value=2,command=valgusfoor)

radio_green = Radiobutton(aken, text="green", bg="green",variable=var,value=3,command=valgusfoor)

nupp.grid(row=1,column=1)
nupp2.grid(row=2,column=1)
nupp3.grid(row=3,column=1)
nupp4.grid(row=4,column=1)
nupp5.grid(row=5,column=1)
nupp6.grid(row=6,column=1)
radio_red.grid(row=1, column=2) 
radio_yellow.grid(row=2, column=2)
radio_green.grid(row=3, column=2)

aken.mainloop()



