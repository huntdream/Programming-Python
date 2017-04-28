from tkinter import *
from tkinter.messagebox import showinfo


def reply():
    showinfo(title='popup', message='Button Pressed')


window = Tk()

button = Button(window, text='Press', command=reply)
button.pack()
Label(text="Press the button above").pack()
window.mainloop()
