from tkinter import Button
class GameButton(Button):
#classdocs
#extends tkinter.Button to be able to store a value.
#Class currently adds no value and could be replaced with tkinter.Button.


    def __init__(self, master, brick):
        Button.__init__(self, master)
        self.brick = brick

    # Currently not used            
    def get_brick(self):
        return self.brick
        