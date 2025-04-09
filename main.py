import tkinter
from tkinter import *
from PIL import Image, ImageTk

# Begin drag
def drag_start(event):
    widget = event.widget
    widget._drag_start_x = event.x
    widget._drag_start_y = event.y
    
# Continue drag
def drag_motion(event):
    widget = event.widget
    x = event.x - widget._drag_start_x
    y = event.y - widget._drag_start_y
    canvas.move(rectangle, x, y)
    widget._drag_start_x = event.x
    widget._drag_start_y = event.y

# Initialise
root = Tk()

# geometry of tkinter frame
root.geometry("700x450")

# Create a canvas
canvas = Canvas(root, width=600, height=400)
canvas.pack()

# Display image on canvas
dragon = Image.open('sample-image.jpg')
img = ImageTk.PhotoImage(dragon)
canvas.create_image(250, 250, anchor=CENTER, image=img)

# Create a draggable rectangle
rectangle = canvas.create_rectangle(10, 10, 50, 50, fill="green")

# Handle movement of rectangle
canvas.tag_bind(rectangle, "<Button-1>", drag_start)
canvas.tag_bind(rectangle, "<B1-Motion>", drag_motion)

# Keep app running
root.mainloop()