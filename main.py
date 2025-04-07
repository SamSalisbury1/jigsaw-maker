import tkinter
from tkinter import *
from PIL import Image, ImageTk

root = Tk()

# Create photo image
dragon = Image.open('sample-image.jpg')
test = ImageTk.PhotoImage(dragon)
label = tkinter.Label(image=test)
label.image = test

# Position
label.place(x=0, y=0)
root.mainloop()
