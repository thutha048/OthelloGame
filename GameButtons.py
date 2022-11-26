from tkinter import E, W, N, S, Frame, PhotoImage
from GameButton import GameButton
class GameButtons(Frame):
# Create a frame with the buttons for the game, is used by GameFrame
    def __init__(self, click):
        super().__init__()
        self.buttons = [[0 for _ in range(8)]for _ in range(8)]
        for x in range(8):
            for y in range(8):
                b = GameButton(self, 0)
                b.grid(row = x, column = y,sticky=(N, S, E, W))
                b.configure( command = lambda row = x, col = y: click(row, col)) #add text = "%s%s"%(x,y) if want present index of btn
                
                self.buttons[x][y] = b
                self.columnconfigure(y, weight = 1)
            self.rowconfigure(x, weight = 1)
        self.reset_board()

    def change_color(self, x, y, color):
        self.buttons[x][y].configure(bg = color)

    def get_brick(self, x, y):
        return self.buttons[x][y].get_brick()

    def reset_board(self):
        for x in range(8):
            for y in range(8):
                self.buttons[x][y].configure(bg = "green")

        self.buttons[3][3].configure(bg = "white")
        self.buttons[4][4].configure(bg = "white")
        self.buttons[4][3].configure(bg = "black")
        self.buttons[3][4].configure(bg = "black")


    