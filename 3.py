import tkinter
import random


root = tkinter.Tk()
canvas = tkinter.Canvas(root, height=600, width=800, bg="black")
canvas.pack()


for i in range(800):
    length = random.randint(1, 100)
    if length > 50:
        canvas.create_line(i, 600, i, 600-length, fill='green')
    else:
        canvas.create_line(i, 600, i, 600 -length, fill='yellow')


root.mainloop()
