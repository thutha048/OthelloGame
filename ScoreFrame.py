from tkinter import Frame, StringVar, E,W, Label
import tkinter

FONT = ('Helvetica', 15)

class ScoreFrame(Frame):

#Set up a frame where scores are displayed. (Current amount of black/white and empty bricks)
#Class used by and added to GameFrame

    def __init__(self, params):
        '''
        Constructor
        Set up StringVars and add them to the labels
        '''

        super().__init__()
        self.whiteTextVar = StringVar()
        self.blackTextVar = StringVar()
        self.emptyTextVar = StringVar()
        self.columnconfigure(0, weight = 1)
        self.columnconfigure(1, weight = 1)
        self.columnconfigure(2, weight = 1)
        self.whiteTextVar.set("WHITE: ")
        self.blackTextVar.set("BLACK: ")
        self.emptyTextVar.set("EMPTY: ")
        self.whiteCount = Label(self, textvariable = self.whiteTextVar, bg = "white", width=3, font=FONT)
        self.whiteCount.grid(row = 0, column = 0, sticky=(E, W))
        self.blackCount = Label(self, textvariable = self.blackTextVar, bg = "gray",width=3, font=FONT)
        self.blackCount.grid(row = 0, column = 1, sticky=(E, W))
        self.emptyCount = Label(self, textvariable = self.emptyTextVar, bg = "yellow", width=3, font=FONT)
        self.emptyCount.grid(row = 0, column = 2,  sticky=(E, W))
        self.status_text = StringVar()
        self.status_text.set("")
        self.status_bar = Label(self, textvariable = self.status_text, width=3, font=FONT)
        self.status_bar.grid(row = 1, column = 0, columnspan = 3, sticky=(E,W))

       



    # Change the textVariables to update the text.
    def update_texts(self, white, black, empty):
        self.whiteTextVar.set("WHITE: %s" %white)
        self.blackTextVar.set("BLACK: %s" %black)
        self.emptyTextVar.set("EMPTY: %s" %empty)

    def update_status(self, text):
        self.status_text.set(text)

