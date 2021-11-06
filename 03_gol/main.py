from tkinter import *
from Cell import Cell
from time import *
import argparse

# Parse arguments and set Matrix size
parser = argparse.ArgumentParser()
parser.add_argument('--size',
                    default=[50, 50],
                    dest='size',
                    help='Define the matrix size. Range: 10-300',
                    type=int,
                    nargs=2
                    )
args = parser.parse_args()
if args.size[0] < 10 or args.size[1] < 10:
    print("WARNING! Minimal size: 10x10, maximal: 300x300.")
    quit()

WIDTH = args.size[0]    #default 50
HEIGHT = args.size[1]   #default 50
WIDTH_MAX_INDEX = WIDTH - 1
HEIGHT_MAX_INDEX = HEIGHT - 1
CELL_SIZE = 10
DELAY_IN_SECONDS = 0.5  #Controls animation speed
next_step_time = 0.0
next_draw_time = 0.0
is_on = False       #controls iteratons
is_running = True   #controls main loop of the program
cell_grid = []



def start():
    global is_on, next_step_time
    is_on = True
    next_step_time = time()

def stop():
    global is_on
    is_on = False

def reset():
    stop()
    for i in range(0, HEIGHT):
        for j in range(0, WIDTH):
            cell_grid[i][j].changeState(False)
            cell_grid[i][j].next_state = False

def create_grid():
    for i in range(0, HEIGHT):
        l = []

        for j in range(0, WIDTH):
            l.append(Cell(c, j, i, CELL_SIZE,0))

        cell_grid.append(l)
        #print(j)

def count_neighbors(row, col):
    # Specify neighbors and count how many of them are alive(active).
    # Note that the plane is used here as a sphere:
    # The ceiling connects with the floor
    # and the right side connects with the left.

    #Find indexes
    right = col + 1
    if right > WIDTH_MAX_INDEX:
        right = 0

    left = col - 1
    if left < 0:
        left = WIDTH_MAX_INDEX

    up = row - 1
    if up < 0:
        up = HEIGHT_MAX_INDEX

    down = row + 1
    if down > HEIGHT_MAX_INDEX:
        down = 0

    neighbors_alive = 0
    ''' Checks neighborhood in this pattern:
            * X *
            X * X
            * X *
    '''
    if cell_grid[row][left].state == True:
        neighbors_alive += 1
    if cell_grid[row][right].state == True:
        neighbors_alive += 1
    if cell_grid[up][col].state == True:
        neighbors_alive += 1
    if cell_grid[down][col].state == True:
        neighbors_alive += 1

    ''' Checks neighborhood in this pattern:
            X * X
            * * *
            X * X
    '''
    if cell_grid[up][left].state == True:
        neighbors_alive += 1
    if cell_grid[up][right].state == True:
        neighbors_alive += 1
    if cell_grid[down][left].state == True:
        neighbors_alive += 1
    if cell_grid[down][right].state == True:
        neighbors_alive += 1

    return neighbors_alive

def check_grid():
    for i in range(0, HEIGHT):
        for j in range(0, WIDTH):
            neighbors = count_neighbors(i, j)
            cell_grid[i][j].checkRules(neighbors)

def next_step():
    for i in range(0, HEIGHT):
        for j in range(0, WIDTH):
            cell_grid[i][j].step()

def onCanvasClick(event):
    row = int(event.x / 10)
    col = int(event.y / 10)
    cell_grid[col][row].alternateState()
    #print('Got canvas click', event.x, event.y, event.widget)

def on_closing():
    global is_running
    is_running = False


# Create UI elements
okno = Tk()
okno.title("John Conway's Game of Life")

frame1 = Frame(okno)
frame1.grid(row=0, column=0)
frame2 = Frame(okno)
frame2.grid(row=0,column=1)

c = Canvas(frame1, width = WIDTH*CELL_SIZE, height=HEIGHT*CELL_SIZE)
c.pack()

btn_start = Button(frame2, text="START", width=8, bg = "green", fg = "white", command=start)
btn_start.pack(pady = 5, padx = 5)
btn_stop = Button(frame2, text="STOP", width=8, bg = "red", fg = "white", command=stop)
btn_stop.pack(pady = 5, padx = 5)
btn_reset = Button(frame2, text="RESET", width=8, bg = "brown", fg = "white", command=reset)
btn_reset.pack(pady = 5, padx = 5)

# Bind and set
okno.protocol("WM_DELETE_WINDOW", on_closing)
c.bind('<Button-1>', onCanvasClick)
create_grid()

# Mainloop
while is_running:
    okno.update()
    if (next_step_time < time() ) and is_on:
        check_grid()
        next_step()
        next_step_time += DELAY_IN_SECONDS

okno.destroy()