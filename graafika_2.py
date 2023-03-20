from tkinter import *
def eesti():
    nupp.configure()
    raam.create_rectangle(190,100,  10,25, fill="blue")
    raam.create_rectangle(190,100,  10,60, fill="black")
    raam.create_rectangle(190,100,  10,135, fill="white")

def baham():
    nupp2.configure()
    raam.create_rectangle(190,100,  400,25, fill="#67c1cf")
    raam.create_rectangle(190,100,  400,60, fill="yellow")
    raam.create_rectangle(190,100,  400,135, fill="#67c1cf")
    raam.create_polygon(190,25,  190,135,  300,80, fill="black")

tekst="Aken"
aken=Tk()
aken.geometry("800x900")  #разрешение экрана
aken.title(tekst)          #заголовок
raam=Canvas(aken,
            width=600,
            height=400,
            bg="white",)
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

nupp2.pack()
nupp.pack()
raam.pack()
aken.mainloop()


