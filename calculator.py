rom sys import exception
from tkinter import *
def click(event):
    text=event.widget.cget("text")
    global scvalue
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value=int(scvalue.get())
        else:
            try:
                value=eval(scvalue.get())
            except Exception as e:
                print(e)
                scvalue.set("error")
                screen.update()

        scvalue.set(value)
        screen.update()

    elif text == "C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

root = Tk()
root.geometry("644x700")
root.title("Calculator with sakii")

scvalue=StringVar()
scvalue.set("")
screen=Entry(root,textvariable=scvalue,font=("lucid 40 bold"))
screen.pack(fill="x",ipady=8,pady=10,padx=10)


f=Frame(root,bg="grey")
b=Button(f,text="9",padx=10,pady=12,font="lucida 20 bold")
b.pack(side="left",padx=18,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="8",padx=12,pady=12,font="lucida 20 bold")
b.pack(side="left",padx=18,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="7",padx=10,pady=12,font="lucida 20 bold")
b.pack(side="left",padx=18,pady=5)
b.bind("<Button-1>",click)

f.pack()

f=Frame(root,bg="grey")
b=Button(f,text="6",padx=10,pady=12,font="lucida 20 bold")
b.pack(side="left",padx=18,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="5",padx=12,pady=12,font="lucida 20 bold")
b.pack(side="left",padx=18,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="4",padx=10,pady=12,font="lucida 20 bold")
b.pack(side="left",padx=18,pady=5)
b.bind("<Button-1>",click)

f.pack()

f=Frame(root,bg="grey")
b=Button(f,text="3",padx=10,pady=12,font="lucida 20 bold")
b.pack(side="left",padx=18,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="2",padx=12,pady=12,font="lucida 20 bold")
b.pack(side="left",padx=18,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="1",padx=10,pady=12,font="lucida 20 bold")
b.pack(side="left",padx=18,pady=5)
b.bind("<Button-1>",click)

f.pack()

f=Frame(root,bg="grey")
b=Button(f,text="0",padx=11,pady=12,font="lucida 20 bold")
b.pack(side="left",padx=18,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="-",padx=14,pady=12,font="lucida 20 bold")
b.pack(side="left",padx=18,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="*",padx=11,pady=12,font="lucida 20 bold")
b.pack(side="left",padx=18,pady=5)
b.bind("<Button-1>",click)

f.pack()

f=Frame(root,bg="grey")
b=Button(f,text="/",padx=10,pady=12,font="lucida 20 bold")
b.pack(side="left",padx=18,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="%",padx=11,pady=12,font="lucida 20 bold")
b.pack(side="left",padx=18,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="=",padx=10,pady=12,font="lucida 20 bold")
b.pack(side="left",padx=18,pady=5)
b.bind("<Button-1>",click)

f.pack()

f=Frame(root,bg="grey")
b=Button(f,text="C",padx=11,pady=12,font="lucida 20 bold")
b.pack(side="left",padx=18,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="+",padx=11,pady=12,font="lucida 20 bold")
b.pack(side="left",padx=18,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text=".",padx=11,pady=12,font="lucida 20 bold")
b.pack(side="left",padx=18,pady=5)
b.bind("<Button-1>",click)

f.pack()

root.mainloop()
