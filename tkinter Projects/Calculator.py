from tkinter import *


def click(event):
    global scvalue
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value = eval(screen.get())
        scvalue.set(value)
        screen.update()

    elif text == "C":
     scvalue.set('')
     screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()


root = Tk()
root.geometry("644x900")
root.title("Calculator Made By Preyas")
root.wm_iconbitmap("Wineass-Ios7-Redesign-Calculator.ico")
scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="lucida 40 bold")
screen.pack(fill=X, ipadx=8, pady=7, padx=10)
f = Frame(root, bg="orange")
b = Button(f, text="9", bg="yellow",  padx=14, pady=2, font="lucida 35 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=10, pady=5)
f.pack()
b = Button(f, text="8", bg="yellow",  padx=14, pady=2, font="lucida 35 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=10, pady=5)
f.pack()
b = Button(f, text="7", bg="yellow",  padx=14, pady=2, font="lucida 35 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=10, pady=5)
f.pack()
f = Frame(root, bg="orange")
b = Button(f, text="6", bg="yellow", padx=14, pady=2, font="lucida 35 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=10, pady=5)
f.pack()
b = Button(f, text="5", bg="yellow", padx=14, pady=2, font="lucida 35 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=10, pady=5)
f.pack()
b = Button(f, text="4", bg="yellow", padx=14, pady=2, font="lucida 35 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=10, pady=5)
f.pack()
f = Frame(root, bg="orange")
b = Button(f, text="3", bg="yellow",  padx=14, pady=2, font="lucida 35 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=10, pady=5)
f.pack()
b = Button(f, text="2", bg="yellow", padx=14, pady=2, font="lucida 35 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=10, pady=5)
f.pack()
b = Button(f, text="1", bg="yellow",  padx=14, pady=2, font="lucida 35 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=10, pady=5)
f.pack()

f = Frame(root, bg="orange")
b = Button(f, text="0", bg="yellow",  padx=15, pady=2, font="lucida 35 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=10, pady=5)
f.pack()
b = Button(f, text="-", bg="yellow",  padx=18, pady=2, font="lucida 35 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=10, pady=5)
f.pack()
b = Button(f, text="*", bg="yellow",  padx=18, pady=2, font="lucida 35 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=10, pady=5)
f.pack()
f = Frame(root, bg="orange")
b = Button(f, text="/", bg="yellow", padx=20, pady=2, font="lucida 35 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=10, pady=5)
f.pack()
b = Button(f, text="%", bg="yellow",  padx=6, pady=2, font="lucida 35 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=10, pady=5)
f.pack()
b = Button(f, text="+", bg="yellow", padx=14, pady=2, font="lucida 35 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=10, pady=5)
f.pack()

f = Frame(root, bg="orange")
b = Button(f, text="C", bg="yellow",  padx=14, pady=2, font="lucida 35 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=10, pady=5)
f.pack()
b = Button(f, text=".", bg="yellow", padx=14, pady=2, font="lucida 35 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=10, pady=5)
f.pack()
b = Button(f, text="=", bg="yellow",  padx=16, pady=2, font="lucida 35 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=10, pady=5)
f.pack()

root.mainloop()