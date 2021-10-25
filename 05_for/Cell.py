from random import randint, random
'''
Stany komórek:
0 - pusta
1 - drzewo
2 - pożar
3 - zbiornik wodny
'''
class Cell():
    lightning_chance = 0.000001
    seed_chance = 0.001
    fire_spread_chance = 0.75

    def __init__ (self, canvas, row, col, size):
        x = col * size
        y = row * size
        self.square = canvas.create_rectangle(x, y, x+size, y+size, outline="white", fill="gray")
        self.canvas = canvas
        # ustawienie początkowego zalesienia
        if randint(0, 100) < 50:
            self.state = 1
            self.next_state = 1
        else:
            self.state = 0
            self.next_state = 0


    def change_state(self):
        if self.state == 3:
            self.state = 0
            self.canvas.itemconfig(self.square, fill="black")
        else:
            self.state = 3
            self.canvas.itemconfig(self.square, fill="blue")


    def Rules(self, neighbours, burning):
        #dla pustego
        if self.state == 0:
            if neighbours < 6:
               if random() < (self.seed_chance*(1+neighbours) ):
                   self.next_state = 1
        #dla drzewa
        elif self.state == 1:
            if burning > 0 and random() < self.fire_spread_chance:
                self.next_state = 2
            elif random() < self.lightning_chance:
                self.next_state = 2
        #dla ognia
        elif self.state == 2:
            self.next_state = 0
        #dla wody
        elif self.state == 3:
            self.next_state = 3

    def step(self):
        self.state = self.next_state
        # decyzja jak pokolorować komórkę
        if self.state == 0:
            self.canvas.itemconfig(self.square, fill="black")

        elif self.state == 1:
            self.canvas.itemconfig(self.square, fill="green")

        elif self.state == 2:
            self.canvas.itemconfig(self.square, fill="red")








