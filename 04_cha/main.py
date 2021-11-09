import tkinter
from tkinter import *
from random import randint,choice
from Shape import Triangle, Square, Pentagon

CANVAS_HEIGHT = 1000
CANVAS_WIDTH = 1400
# shape = Triangle(plane_size=(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT))
# shape = Square(plane_size=(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT))
shape = Pentagon(plane_size=(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT))
step_counter = 0
is_on = False
is_running = True
point = shape.get_random_point_inside()

def start():
    global is_on
    is_on = True

def stop():
    global is_on
    is_on = False

def reset(canvas: tkinter.Canvas, counter_label: tkinter.Label):
    global step_counter
    step_counter = 0
    stop()
    canvas.delete('all')
    counter_label.configure(text=str(step_counter))
    canvas.create_polygon(shape.get_all_polygon_vertices(), outline="white")
    make_next_point(shape.get_next_vertice())

def make_next_point(vertex):
    global point
    vertex = shape.get_next_vertice()
    new_x = (vertex[0] + point[0]) // 2
    new_y = (vertex[1] + point[1]) // 2
    point = [new_x, new_y]

def on_closing():
    global is_running
    is_running = False



window = Tk()
frame1 = Frame(window)
frame1.grid(row = 0, column = 0)
frame2 = Frame(window)
frame2.grid(row = 0, column = 1)

canvas = Canvas(frame1, height = CANVAS_HEIGHT, width = CANVAS_WIDTH, bg="black")
canvas.pack()
label1 = Label(frame2, text="Step:", font=("Arial",12) )
label1.pack()
label2 = Label(frame2, text="0", font=("Arial",12) )
label2.pack(pady = 10)
btn_start = Button(frame2, text="START", bg= "green", fg="white", command=start)
btn_start.pack(pady=5)
btn_stop = Button(frame2, text="STOP", bg= "red", fg="white", command=stop)
btn_stop.pack(pady=5)
btn_reset = Button(frame2, text="RESET", bg= "brown", fg="white", command=lambda: reset(canvas, label2))
btn_reset.pack(pady=5)

#Create RECTANGLE
# canvas.create_polygon([vertex1[0], vertex1[1], vertex2[0], vertex2[1], vertex3[0], vertex3[1] ],
#                         outline="white")
# canvas.create_polygon( shape.get_all_polygon_vertices(), outline="white")

#Make first iteration
# make_next_point(shape.get_next_vertice())

reset(canvas, label2)

window.protocol("WM_DELETE_WINDOW", on_closing)


#mainloop
while is_running:
    window.update()
    if is_on:
        make_next_point(shape.get_next_vertice() )
        canvas.create_rectangle(point[0], point[1], point[0], point[1], outline="white",fill="white")
        step_counter += 1
        label2.configure(text=str(step_counter))




#window.mainloop()