from tkinter import *
from Cell import Cell
from time import *
import argparse

# Parse arguments
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

WIDTH = args.size[0]
HEIGHT = args.size[1]
W_index = WIDTH - 1
H_index = HEIGHT - 1
NEXT_STEP_TIME = 0.0
NEXT_DRAW_TIME = 0.0
DELAY_IN_SECONDS = 0.5
IS_ON = False
cell_grid = []
cell_size = 10



def start():
    global IS_ON
    IS_ON = True
    NEXT_STEP_TIME = time()

def stop():
    global IS_ON
    IS_ON = False

def reset():
    stop()
    for i in range(0, HEIGHT):
        for j in range(0, WIDTH):
            cell_grid[i][j].changeState(False)
            cell_grid[i][j].next_state = False


okno = Tk()
#okno.geometry("600x600")
okno.title("John Conway's Game of Life")

frame1 = Frame(okno)
frame1.grid(row=0, column=0)
frame2 = Frame(okno)
frame2.grid(row=0,column=1)

c = Canvas(frame1, width = WIDTH*cell_size, height=HEIGHT*cell_size)
c.pack()

btn_start = Button(frame2, text="START", width=8, bg = "green", fg = "white", command=start)
btn_start.pack(pady = 5, padx = 5)
btn_stop = Button(frame2, text="STOP", width=8, bg = "red", fg = "white", command=stop)
btn_stop.pack(pady = 5, padx = 5)
btn_reset = Button(frame2, text="RESET", width=8, bg = "brown", fg = "white", command=reset)
btn_reset.pack(pady = 5, padx = 5)

def create_grid():
    for i in range(0, HEIGHT):
        l = []

        for j in range(0, WIDTH):
            l.append(Cell(c, j, i, cell_size,0))

        cell_grid.append(l)
        print(j)

def count_neighbours(row, col):
    #PRAWY
    right = col + 1
    if right > W_index:
        right = 0

    #LEWY
    left = col - 1
    if left < 0:
        left = W_index

    #GÓRNY
    up = row - 1
    if up < 0:
        up = H_index

    #DOLNY
    down = row + 1
    if down > H_index:
        down = 0

    #SPRAWDZENIE ILOŚCI
    count = 0
    '''     * X *
            X * X
            * X *
    '''
    if cell_grid[row][left].state == True:
        count += 1
    if cell_grid[row][right].state == True:
        count += 1
    if cell_grid[up][col].state == True:
        count += 1
    if cell_grid[down][col].state == True:
        count += 1

    '''     X * X
            * * *
            X * X
    '''
    if cell_grid[up][left].state == True:
        count += 1
    if cell_grid[up][right].state == True:
        count += 1
    if cell_grid[down][left].state == True:
        count += 1
    if cell_grid[down][right].state == True:
        count += 1

    return count

def check_grid():
    for i in range(0, HEIGHT):
        for j in range(0, WIDTH):
            neighbours = count_neighbours(i, j)
            cell_grid[i][j].checkRules(neighbours)

def next_step():
    for i in range(0, HEIGHT):
        for j in range(0, WIDTH):
            cell_grid[i][j].step()

def onCanvasClick(event):
    row = int(event.x / 10)
    col = int(event.y / 10)
    cell_grid[col][row].alternateState()
    print('Got canvas click', event.x, event.y, event.widget)

c.bind('<Button-1>', onCanvasClick)

create_grid()

'''
for i in range(0, HEIGHT):
    print( str(i) + ", " + str(len(cell_grid[i])) )

'''
#NEXT_STEP_TIME = time() + DELAY_IN_SECONDS
while True:
    okno.update()
    '''
    if NEXT_DRAW_TIME < time():
        okno.update()
        NEXT_DRAW_TIME += 0.1
    '''
    if (NEXT_STEP_TIME < time() ) and IS_ON:
        check_grid()
        next_step()
        #c.update()
        NEXT_STEP_TIME += DELAY_IN_SECONDS