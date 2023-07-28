from tkinter import*
from PIL import Image,ImageTk
preyas_root = Tk()
preyas_root.geometry("2255x744")
# for jpg Image
image = Image.open("D:\Preyas\images\shahrukh-khan_2.jpg")
photo= ImageTk.PhotoImage(image)
# photo = PhotoImage(file ="D:\Preyas\images\dsBuffer.png")
varun_label = Label(image=photo)
varun_label.pack() 

preyas_root.mainloop()
