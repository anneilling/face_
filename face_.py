from tkinter import *

def lisa_nina():
    if var_nina.get()=="Nina":
        c.create_oval((225, 225, 275, 275), fill="crimson", outline="black") #нос
    elif var_nina.get()=="tühi":
        c.create_oval((225, 225, 275, 275), fill="thistle", outline="thistle") #нос
def lisa_suu():
    if var_suu.get()=="Suu":
        c.create_arc((100, 300, 400,400),start=180,extent=180, style=ARC, fill="black",width=10, outline="black")
    elif var_suu.get()=="tühi":
        c.create_arc((100, 300, 400,400),start=180,extent=180, style=ARC,   fill="thistle",width=10, outline="thistle")
def lisa_eyes():
    if var_eyes.get()=="Silmad":
        c.create_oval((300, 100, 400, 200), fill="whitesmoke", outline="black") #првый глаз
        c.create_oval((375, 175, 325, 125), fill="black", outline="black") #првый глаз
        c.create_oval((200, 200, 100, 100), fill="whitesmoke", outline="black") #левый глаз
        c.create_oval((125, 125, 175, 175), fill="black", outline="black") #првый глаз
    elif var_eyes.get()=="tühi":
        c.create_oval((300, 100, 400, 200),  fill="thistle", outline="thistle") #првый глаз
        c.create_oval((200, 200, 100, 100),  fill="thistle", outline="thistle") #левый глаз
def lisa_nao():
    if var_nao.get()=="Nägu":
        c.create_oval((10, 10, 490, 490), fill="lavender", outline="black") #лицо
    elif var_nao.get()=="tühi":
        c.create_oval((10, 10, 490, 490), fill="thistle", outline="thistle") #лицо
aken=Tk()
aken.title("Face")
aken.geometry('800x600')
aken.configure(bg="mediumslateblue")
aken.grab_set()
lbl=Label(aken,text="<3",height=2,width=30,font="Arial 20",fg="blueviolet",bg="aliceblue",relief=GROOVE)    
c = Canvas(aken, width=500, height=500, bg="thistle")
var_nina=StringVar()
ch_nina=Checkbutton(aken,text="Nina", variable=var_nina, onvalue="Nina", offvalue="tühi",bg="lightsteelblue",command=lisa_nina)
ch_nina.pack(side=RIGHT)
var_suu=StringVar()
ch_suu=Checkbutton(aken,text="Suu", variable=var_suu, onvalue="Suu", offvalue="tühi",bg="lightsteelblue",command=lisa_suu)
ch_suu.pack(side=RIGHT)
var_eyes=StringVar()
ch_eyes=Checkbutton(aken,text="Silmad", variable=var_eyes, onvalue="Silmad", offvalue="tühi",bg="lightsteelblue",command=lisa_eyes)
ch_eyes.pack(side=RIGHT)
var_nao=StringVar()
ch_nao=Checkbutton(aken,text="Nägu", variable=var_nao, onvalue="Nägu", offvalue="tühi",bg="lightsteelblue",command=lisa_nao)
ch_nao.pack(side=RIGHT)

c.pack(side=RIGHT)
lbl.pack()
aken.mainloop()


