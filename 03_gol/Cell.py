class Cell():

    def __init__(self, canvas, row, col, cellSize,cellType):
        x = row*cellSize
        y = col*cellSize
        self.square = canvas.create_rectangle(x, y, x+cellSize,y+cellSize, outline="white", fill="grey")
        self.cellType = cellType
        self.canvas = canvas
        self.state = False
        self.next_state = False

    def changeState(self, willLive):
        if willLive == True:
            self.state = True
            self.canvas.itemconfig(self.square, fill = "orange")
        else:
            self.state = False
            self.canvas.itemconfig(self.square, fill = "grey")

    def alternateState(self):
        if self.state == True:
            self.changeState(False)
        else:
            self.changeState(True)

    def step(self):
        self.changeState(self.next_state)

    def checkRules(self, neighbours):
        if self.state == True:
            if neighbours >= 2 and neighbours <= 3:
                self.next_state = True
            else:
                self.next_state = False
        else:
            if neighbours == 3:
                self.next_state = True
