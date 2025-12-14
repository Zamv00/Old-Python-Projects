from tkinter import *
from tkinter import colorchooser

def start_draw(event):
    try:
        global prev_x, prev_y
        prev_x, prev_y = event.x, event.y
    except Exception as e:
        print("An error has occured: ", e)
def change_color():
    global color
    try:
        color = colorchooser.askcolor()[1]
    except Exception as e:
        print("An error has occured: ", e)
def change_background_color():
    global bg_color
    try:
        bg_color = colorchooser.askcolor()[1]
        canvas.config(bg=bg_color)
    except Exception as e:
        print("An error has occured: ", e)
def draw(event):
    global prev_x, prev_y, color, brush_size
    try:
        x, y = event.x, event.y
        canvas.create_line(prev_x, prev_y, x, y, fill=color, width=brush_size, smooth=True)
        prev_x, prev_y = x, y
    except Exception as e:
        print("An error has occured: ", e)
def update_brush_size(value):
    global brush_size
    try:
        brush_size = int(value)
    except Exception as e:
        print("An error has occured: ", e)

root = Tk()
root.title("Drawing App")
root.geometry("770x600")
root.config(bg="#2E8BC0")
root.resizable(False, False)

color = "black"
bg_color = "white"
brush_size = 5

canvas = Canvas(root, width=500, height=500, bg="white")
canvas.pack(expand=TRUE, fill=BOTH)

canvas.bind("<Button-1>", start_draw)
canvas.bind("<B1-Motion>", draw)

button_frame = Frame(root)
button_frame.config(bg="#2E8BC0")
button_frame.pack(side=BOTTOM, pady=10)

button_color = Button(button_frame, text="Brush Color", command=change_color, font=("Consolas", 12, "bold"), bg="#145DA0", fg="white")
button_color.grid(row=0, column=0, padx=10)

button_bg_color = Button(button_frame, text="Background Color", command=change_background_color, font=("Consolas", 12, "bold"), bg="#145DA0", fg="white")
button_bg_color.grid(row=0, column=1, padx=10)

button_clear = Button(button_frame, text="Clear", command=lambda: canvas.delete("all"), font=("Consolas", 12, "bold"), bg="#145DA0", fg="white")
button_clear.grid(row=0, column=2, padx=10)

label_size = Label(button_frame, text="Brush Size:", font=("Consolas", 12, "bold"), bg="#2E8BC0", fg="white")
label_size.grid(row=0, column=3, padx=5)

size_var = StringVar(root)
size_var.set("5")
size_box = Spinbox(button_frame, from_=1, to=20, textvariable=size_var, width=5, command=lambda: update_brush_size(size_var.get()))
size_box.grid(row=0, column=4, padx=10)




root.mainloop()