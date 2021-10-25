from tkinter import *
from random import randint,choice

def start():
    global is_on
    is_on = True

def stop():
    global is_on
    is_on = False

def make_next_point(vertex):
    global point
    new_x = (vertex[0] + point[0]) // 2
    new_y = (vertex[1] + point[1]) // 2
    point = [new_x, new_y]

vertex1 = (2,868)
vertex2 = (1002,868)
vertex3 = (502,2)
vertex_list = [vertex1, vertex2, vertex3]
point = [-1,-1]

canvas_height = 870
canvas_width = 1004
step_counter = 0
is_on = False

window = Tk()
frame1 = Frame(window)
frame1.grid(row = 0, column = 0)
frame2 = Frame(window)
frame2.grid(row = 0, column = 1)

canvas = Canvas(frame1, height = canvas_height, width = canvas_width, bg="black")
canvas.pack()
label1 = Label(frame2, text="Step:", font=("Arial",12) )
label1.pack()
label2 = Label(frame2, text="0", font=("Arial",12) )
label2.pack(pady = 10)
btn_start = Button(frame2, text="START", bg= "green", fg="white", command=start)
btn_start.pack(pady=5)
btn_stop = Button(frame2, text="STOP", bg= "red", fg="white", command=stop)
btn_stop.pack(pady=5)

#Create RECTANGLE
canvas.create_polygon([vertex1[0], vertex1[1], vertex2[0], vertex2[1], vertex3[0], vertex3[1] ],
                        outline="white")

#Choose first point
point[0] = randint(vertex1[0], vertex2[0])
point[1] = randint(vertex3[1], vertex2[1])

#mainloop
while True:
    window.update()
    if is_on:
        make_next_point(choice(vertex_list) )
        canvas.create_rectangle(point[0], point[1], point[0], point[1], outline="white",fill="white")
        step_counter += 1
        label2.configure(text=str(step_counter) )




#window.mainloop()