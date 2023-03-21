
from math import*
from tkinter import *
import random
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
aken.geometry("1100x500")  #разрешение экрана
aken.title(tekst)          #заголовок

nupp=Button(aken,
            text="Eesti lipp",
            bg="lightblue",          
            fg="#4f1fd1",  
            font="Dubai 20",  
            activebackground="orange",
            activeforeground="red",
            height=3,    
            width=15,
            command=eesti)
nupp2=Button(aken,
            text="Bahama saarte lipp",
            bg="lightblue",          
            fg="#4f1fd1",  
            font="Dubai 20",  
            activebackground="orange",
            activeforeground="red",
            height=3,    
            width=15,
            command=baham)
nupp3=Button(aken,
            text="Muster",
            bg="lightblue",          
            fg="#4f1fd1",  
            font="Dubai 20",  
            activebackground="orange",
            activeforeground="red",
            height=3,    
            width=15,
            command=muster)
nupp4=Button(aken,
            text="Male tahvel",
            bg="lightblue",          
            fg="#4f1fd1",  
            font="Dubai 20",  
            activebackground="orange",
            activeforeground="red",
            height=3,    
            width=15,
            command=board)
nupp5=Button(aken,
            text="Ringid",
            bg="lightblue",          
            fg="#4f1fd1",  
            font="Dubai 20",  
            activebackground="orange",
            activeforeground="red",
            height=3,    
            width=15,
            command=ringad)

nupp5.pack(side=LEFT)
nupp4.pack(side=LEFT)
nupp3.pack(side=LEFT)
nupp.pack(side=LEFT)
nupp2.pack(side=LEFT)

aken.mainloop()




