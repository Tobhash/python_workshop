from tkinter import *
from Cell import *
from time import time
import datetime

WIDTH = 50
HEIGHT = 50
#zmienne do zbierania danych
total_cells = WIDTH * HEIGHT
tree_cells = 0
empty_cells = 0
burning_cells = 0
water_cells = 0
DATA_FILE_NAME = ""
iteration_number = 1

cell_grid = []
cell_size = 6

Is_ON = False

FPS_Time = 0
FPS_Delay = 0.25

window = Tk()
window.title("Super Mega Nitro AUTOMATOR 3000")

frame1 = Frame(window)
frame1.grid(row = 0, column = 0)
frame2 = Frame(window)
frame2.grid(row = 0, column = 1)

def on():
    global Is_ON
    Is_ON = True

def off():
    global Is_ON
    Is_ON = False

def reset():
    off()
    cell_grid.clear()
    create_grid()




btn_start = Button(frame2, text = "START", bg="green", fg="white", command = on)
btn_start.pack()
btn_stop = Button(frame2, text = "STOP", bg="red", fg="white", command = off)
btn_stop.pack()
btn_reset = Button(frame2, text = "RESET", bg="brown", fg="white", command = reset)
btn_reset.pack()

c = Canvas(frame1, width = WIDTH*cell_size, height = HEIGHT*cell_size, bg="yellow")
c.pack()

#Funkcje
def create_grid():
    for i in range(0, HEIGHT):
        pasek = []
        for j in range(0, WIDTH):
            pasek.append(Cell(c, i, j, cell_size))
        cell_grid.append(pasek)

def canvas_click(event):
    row = int(event.y / cell_size)
    col = int(event.x / cell_size)
    cell_grid[row][col].change_state()

def count_neighbours(row, col):
    #PRAWY
    right = col + 1
    if right == WIDTH:
        right = 0
    #LEWY
    left = col - 1
    if left < 0:
        left = WIDTH-1
    #GÓRNY
    up = row -1
    if up < 0:
        up = HEIGHT - 1
    #DOLNY
    down = row + 1
    if down == HEIGHT:
        down = 0
    #SPRAWDZENIE ILOŚCI AKTYWNYCH SOMSIADUF
    count = 0

    ''' X * X
        * o *
        X * X '''


    if cell_grid[up][left].state == 1:
        count +=1
    if cell_grid[up][right].state == 1:
        count +=1
    if cell_grid[down][left].state == 1:
        count +=1
    if cell_grid[down][right].state == 1:
        count +=1

    ''' * X *
        X o X
        * X * '''

    if cell_grid[up][col].state == 1:
        count +=1
    if cell_grid[row][left].state == 1:
        count +=1
    if cell_grid[down][col].state == 1:
        count +=1
    if cell_grid[row][right].state == 1:
        count +=1

    # sprawdzenie pożaru w okolicy
    burning = 0
    ''' X * X
        * o *
        X * X '''
    if cell_grid[up][left].state == 2:
        burning +=1
    if cell_grid[up][right].state == 2:
        burning +=1
    if cell_grid[down][left].state == 2:
        burning +=1
    if cell_grid[down][right].state == 2:
        burning +=1

    ''' * X *
        X o X
        * X * '''

    if cell_grid[up][col].state == 2:
        burning +=1
    if cell_grid[row][left].state == 2:
        burning +=1
    if cell_grid[down][col].state == 2:
        burning +=1
    if cell_grid[row][right].state == 2:
        burning +=1

    return [count, burning]



def check_grid():
    global tree_cells, empty_cells, burning_cells, water_cells
    for i in range(0, HEIGHT):
        for j in range(0, WIDTH):
            zywy_somsiad = count_neighbours(i,j)
            cell_grid[i][j].Rules(zywy_somsiad[0], zywy_somsiad[1])

            cell_state = cell_grid[i][j].state
            if cell_state == 0:
                empty_cells += 1
            elif cell_state == 1:
                tree_cells += 1
            elif cell_state == 2:
                burning_cells += 1
            else:
                water_cells += 1

def next_step():
    for i in range(0, HEIGHT):
        for j in range(0, WIDTH):
            cell_grid[i][j].step()

def collect_data():
    global total_cells, tree_cells, empty_cells, burning_cells, water_cells
    global DATA_FILE_NAME, iteration_number
    # na początku podajemy numer iteracji i tabulator dla wyrównania
    data = "[" + str(iteration_number) + "]\t"
    #procent drzew
    data += "Trees: "
    data += "{:.2f}".format((tree_cells/total_cells) * 100)
    data += "%, "
    #procent pustych
    data += "Empty: "
    data += "{:.2f}".format((empty_cells/total_cells) * 100)
    data += "%, "
    #procent płonących
    data += "Burning: "
    data += "{:.2f}".format((burning_cells/total_cells) * 100)
    data += "%, "
    #procent zbiorników wodnych
    data += "Water: "
    data += "{:.2f}".format((water_cells/total_cells) * 100)
    data += "%, "
    #print(data)
    data += "\n"
    # zapisujemy dane do wskazanego pliku. Parametr 'a' oznacza, że
    # chcemy dopisać coś na koniec istniejącego już pliku
    # po słowie 'as' podajemy nazwę zmiennej pod jaką będziemy mogli
    # używać właśnie otwartego pliku
    with open(DATA_FILE_NAME, 'a') as plik:
        plik.write(data)

    #zwiększamy numer iteracji o jeden
    iteration_number += 1
    #reset variables
    tree_cells = empty_cells = burning_cells = water_cells = 0


def create_file():
    global DATA_FILE_NAME
    #zapisujemy informacje o dacie i czasie do zmiennej d
    d = datetime.datetime.now()
    #tworzymy zmienną pomocniczą t
    t = ""
    t += str(d.year) + "_" + str(d.month) + "_" + str(d.day)
    t += "@"
    t += str(d.hour) + "_" + str(d.minute) + "_" + str(d.second)
    t += ".txt"
    #przypisujemy nazwę pliku do odpowiedniej zmiennej
    DATA_FILE_NAME = t
    print(DATA_FILE_NAME)
    # tworzymy plik o podanej nazwie. Parametr 'x' oznacza, że chcemy
    # tylko stworzyć nowy plik.
    # dzięki składni "with" nie musimy pamiętać o zamknięciu pliku
    # bo Python zrobi to za nas
    with open(DATA_FILE_NAME,'x'):
        pass

#Pętla
create_grid()
c.bind('<Button-1>', canvas_click)
create_file()
while True:
    window.update()
    if FPS_Time < time() and Is_ON:
        FPS_Time = time() + FPS_Delay
        check_grid()
        collect_data()
        next_step()


