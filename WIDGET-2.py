from tkinter import *

class MyWindow:
    def __init__(self, win):
        self.txt1 = Entry(win, bd=1)
        self.txt1.place(x=90, y=35)

window = Tk()
mywin = MyWindow(window)
window.title("Field Text")
window.geometry("300x100+10+10")
window.mainloop()