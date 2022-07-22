from tkinter import*
import random as r


def yap():
    c.delete("all")
    h=[]
    for i in range(0,5):
        h.append(chr(r.randint(65,90)))

    fnt=["Verdana","Papyrus","Arial","Calibri"]
    renk=["purple","black","green","gray","blue"]

    t1=c.create_text(40+r.randint(0,10),40+r.randint(0,10),font=fnt[r.randint(0,3)]+" 32 bold",text=h[0],fill=renk[r.randint(0,4)])
    t2=c.create_text(80+r.randint(0,10),40+r.randint(0,10),font=fnt[r.randint(0,3)]+" 32 bold",text=h[1],fill=renk[r.randint(0,4)])
    t3=c.create_text(120+r.randint(0,10),40+r.randint(0,10),font=fnt[r.randint(0,3)]+" 32 bold",text=h[2],fill=renk[r.randint(0,4)])
    t4=c.create_text(160+r.randint(0,10),40+r.randint(0,10),font=fnt[r.randint(0,3)]+" 32 bold",text=h[3],fill=renk[r.randint(0,4)])
    t5=c.create_text(200+r.randint(0,10),40+r.randint(0,10),font=fnt[r.randint(0,3)]+" 32 bold",text=h[4],fill=renk[r.randint(0,4)])

    for i in range(0,15):
        l=c.create_line(r.randint(5,285),r.randint(5,95),r.randint(5,285),r.randint(5,95),fill=renk[r.randint(0,4)])

pencere=Tk()
pencere.geometry("300x170")


c=Canvas(width=280,height=100,bg="white")
c.place(x=10,y=10)

b=Button(text="Oluştur",font="Verdana 14 bold",command=yap)
b.place(x=100,y=120)






pencere.mainloop()