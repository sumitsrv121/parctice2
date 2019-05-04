from tkinter import *
from tkinter import ttk
window = Tk()
window.geometry('400x400')

#label
lbl = Label(window,text='Hello World',font = ('Tahoma',24))
lbl.grid(column=0,row=0)

#textbox
box = Entry(window,width=20)
box.focus()
box.grid(column=0,row=1)


def func():
    lbl.configure(text=box.get())
#button
btn = Button(window,text='check',command=func,bg="orange",fg="black")
btn.grid(column=1,row=1)

window.mainloop()