from GameButtons import GameButtons
from tkinter import Tk, Frame, BOTH, X
from ScoreFrame import ScoreFrame
from SelectPlayer import SelectPlayer
#from Controller import Controller
from tkinter import E, W, N, S, Frame, PhotoImage
from GameButton import GameButton

import tkinter

class GameFrame(Frame):
# Main UI frame. Starts a Tk() and adds other frames to it.

    def __init__(self, params, click, restart_game, start_game):
        self.root = Tk()
        self.root.geometry("600x750")
        self.scoreFrame = ScoreFrame(self.root)
        self.scoreFrame.update_texts(2, 2, 60)
        self.scoreFrame.pack(fill = X)   
        self.update_status("First turn: black player")
        self.buttons = GameButtons(click)
        self.buttons.pack(fill=BOTH, expand=1)
        self.playerSelect = SelectPlayer(restart_game,start_game)
        self.playerSelect.pack(fill = BOTH)
      

        
    def change_color(self, x, y, color):
        self.buttons.change_color(x, y, color)

    def update_texts(self, white, black, empty):
        self.scoreFrame.update_texts(white, black, empty)

    def start(self):
        self.root.mainloop()

    def reset_board(self):
        self.buttons.reset_board()
    
    def update_status(self, text):
        self.scoreFrame.update_status(text)
    
    
