import tkinter
import random

root = tkinter.Tk()
canvas = tkinter.Canvas(root, height=600, width=800, bg="black")
canvas.pack()


colors = ["green", "blue", "yellow", "black", "orange", "red", "purple"]


def x(event):
    color = random.choice(colors)
    canvas.create_rectangle(event.x-30, event.y-30, event.x+30, event.y+30, fill=color)


def y(event):
    color = random.choice(colors)
    size = random.randint(10, 50)
    canvas.create_oval(event.x-size, event.y-size, event.x+size, event.y+size, fill=color)


abeceda = "abcdefghijklmnopqrstuvwxyz"


def z(event):
    text = random.choice(abeceda)
    canvas.create_text(event.x, event.y, font=("Open Sans", 15), color="white", text=text)


canvas.bind_all("<x>", x)
canvas.bind_all("<y>", y)
canvas.bind_all("<z>", z)

root.mainloop()
