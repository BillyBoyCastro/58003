from tkinter import *

windows = Tk()
label1 = Label(windows, text="Laboratory Activity 5", fg="black", font="Tahoma")
label1.place(x=0, y=20, width=300, height=50)

label2 = Label(windows, text="Submitted to Mam Sayo", fg="black", font="Tahoma")
label2.place(x=0, y=60, width=300, height=50)

windows.geometry("300x120+10+10")
windows.title("Label")
windows.mainloop()


