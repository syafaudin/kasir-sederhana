from tkinter import *
from tkinter import messagebox


app = Tk()
bakso = StringVar()
mie_ayam = StringVar()
es_teh = StringVar()
total = StringVar()
cash = StringVar()
semua = 0

def spinklik():
    global bakso,mie_ayam,es_teh,total,cash,semua
    harga_bakso = int(bakso.get()) * 10000
    harga_mie = int(mie_ayam.get())* 7000
    harga_es = int(es_teh.get())* 5000
    semua = harga_bakso + harga_mie + harga_es
    total.set(str(semua))
    
def tomboltotal():
    
    duit = int(cash.get())
    if duit >= semua:
        kembalian = duit - semua
        messagebox.showinfo(message='Kembalian sebesar Rp{}'.format(int(kembalian)))
    else:
        messagebox.showinfo(message='Uang Kurang')
def tombolreset():
    bakso.set('0')
    mie_ayam.set('0')
    es_teh.set('0')
    total.set('0')
    

app.geometry('700x500')
app.configure(bg='blue')
app.geometry()
#Tag Menu
Label(app,text="WARUNG PAK PYTHON", bg='blue',foreground='black', font='arial 12 bold').place(x =300,y= 50)
Label(app,text="1 -> Bakso", bg='blue',foreground='black', font='arial 12 bold').place(x =100,y= 100)
Label(app,text="2 -> Mie Ayam", bg='blue',foreground='black', font='arial 12 bold').place(x =100,y= 130)
Label(app,text="3 -> ES Teh", bg='blue',foreground='black', font='arial 12 bold').place(x =100,y= 160)
#Tag Harga
Label(app,text="Rp 10000", bg='blue',foreground='black', font='arial 12 bold').place(x =210,y= 100)
Label(app,text="Rp 7000", bg='blue',foreground='black', font='arial 12 bold').place(x =210,y= 130)
Label(app,text="Rp 5000", bg='blue',foreground='black', font='arial 12 bold').place(x =210,y= 160)
Label(app,text="Rp", bg='blue',foreground='black', font='arial 12 bold').place(x =250,y= 190)
Label(app,textvariable=total, bg='blue',foreground='black', font='arial 12 bold').place(x =290,y= 190)
Label(app,text="Total Harga", bg='blue',foreground='black', font='arial 12 bold').place(x =100,y= 190)

#spinbox
Spinbox(app, from_=0, to=100, width=3, font='arial 12 bold', textvariable=bakso, command=spinklik).place(x=300, y=100)
Spinbox(app, from_=0, to=100, width=3, font='arial 12 bold', textvariable=mie_ayam, command=spinklik).place(x=300, y=130)
Spinbox(app, from_=0, to=100, width=3, font='arial 12 bold', textvariable=es_teh,command=spinklik).place(x=300, y=160)

#komponen label
Label(app, text='Masukkan Uang').place(x=100, y=350 )
Entry(app, textvariable=cash).place(x= 300, y=350 )

Button(app, text="Total", bg='green', command=tomboltotal).place(x=370, y=200 )
Button(app, text="Reset", bg='green', command=tombolreset).place(x=430, y=200 )

app.mainloop()