from tkinter import Button
class GameButton(Button):
    def __init__(self, master, brick):
        Button.__init__(self, master)
        self.brick = brick

    # Currently not used            
    def get_brick(self):
        return self.brick
