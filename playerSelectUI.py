from tkinter import Frame, Label, Button, SUNKEN, RAISED, N, S, E, W
FONT = ('Helvetica', 15)


class PlayerSelectUi(Frame):
#Set up a frame where the user can select AI / Human controller for each of the players
#Class used by and added to GameFrame

# Set up the UI that allows player to select difficulty of opponent
# start_new_game is a function passed from Controller
    def __init__(self, start_new_game, start_game):
        #constructor
        super().__init__()
        self.selection1 = [None] * 5
        self.selection2 = [None] * 5
        self.selectedP1 = 4 #default to human controller
        self.selectedP2 = 4

        self.p1label = Label(self, text = "Player 1 (Black)", font=FONT)
        self.p1label.grid(row = 0, column = 0)
        self.selection1[0] = self.player1SelectButton1 = Button(self,bd=3, text = "Easy", fg="green", font=FONT)
        self.player1SelectButton1.grid(row = 0, column = 1,sticky=(N, S, E, W))
        self.player1SelectButton1.configure( command = lambda: self.clickP1(0))
        self.selection1[1] = self.player1SelectButton2 = Button(self,bd=3, text = "Normal", fg="orange", font=FONT)
        self.player1SelectButton2.grid(row = 0, column = 2, sticky = (N, S, E, W))
        self.player1SelectButton2.configure( command = lambda: self.clickP1(1))
        self.selection1[2] = self.player1SelectButton3 = Button(self,bd=3, text = "Hard", fg="red", font=FONT)
        self.player1SelectButton3.grid(row = 0, column = 3,sticky=(N, S, E, W))
        self.player1SelectButton3.configure( command = lambda: self.clickP1(2))
        self.selection1[3] = self.player1SelectButton4 = Button(self,bd=3, text = "MiniMax", fg="deeppink", font=FONT)
        self.player1SelectButton4.grid(row = 0, column = 4,sticky=(N, S, E, W))
        self.player1SelectButton4.configure( command = lambda: self.clickP1(3))
        self.selection1[4] = self.player1SelectButton5 = Button(self,bd=3, text = "Human", font=FONT)
        self.player1SelectButton5.grid(row = 0, column = 5,sticky=(N, S, E, W))
        self.player1SelectButton5.configure( relief = SUNKEN, command = lambda: self.clickP1(4))

        self.p2label = Label(self, text = "Player 2 (White)", font=FONT)
        self.p2label.grid(row = 1, column = 0)
        self.selection2[0] = self.player2SelectButton1 = Button(self,bd=3, text = "Easy", fg="green", font=FONT)
        self.player2SelectButton1.grid(row = 1, column = 1,sticky=(N, S, E, W))
        self.player2SelectButton1.configure(command = lambda: self.clickP2(0))
        self.selection2[1] = self.player2SelectButton2 = Button(self,bd=3, text = "Normal", fg="orange", font=FONT)
        self.player2SelectButton2.grid(row = 1, column = 2, sticky = (N, S, E, W))
        self.player2SelectButton2.configure(command = lambda: self.clickP2(1))
        self.selection2[2] = self.player2SelectButton3 = Button(self,bd=3, text = "Hard", fg="red", font=FONT)
        self.player2SelectButton3.grid(row = 1, column = 3,sticky=(N, S, E, W))
        self.player2SelectButton3.configure(command = lambda: self.clickP2(2))
        self.selection2[3] = self.player2SelectButton4 = Button(self,bd=3, text = "MiniMax", fg="deeppink", font=FONT)
        self.player2SelectButton4.grid(row = 1, column = 4,sticky=(N, S, E, W))
        self.player2SelectButton4.configure( command = lambda: self.clickP2(3))
        self.selection2[4] = self.player2SelectButton5 = Button(self,bd=3, text = "Human", font=FONT)
        self.player2SelectButton5.grid(row = 1, column = 5,sticky=(N, S, E, W))
        self.player2SelectButton5.configure(relief = SUNKEN, command = lambda: self.clickP2(4))

        ##
        #self.menuGame = tkinter.Menu(self,tearoff=0)
        #self.menuGame.add_command(label = 'New Game ', command = self._new_game)
        ##
        self.startGameButton = Button(self, text = "Restart", font=FONT)
        self.startGameButton.grid(row = 2, column = 0,sticky=(N, S, E, W))
        self.startGameButton.configure(
            command = lambda: start_new_game())

        self.startGameButton = Button(self, text = "Start ", font=FONT)
        self.startGameButton.grid(row = 2, column = 1)
        self.startGameButton.configure(
            command = lambda: start_game(self.selectedP1, self.selectedP2))

        #self.reGameButton = Button(self, text = "Restart", font=FONT)
        #self.reGameButton.grid(row = 2, column = 1)
        #self.reGameButton.configure(
         #   command = lambda: start_new_game(self.selectedP1, self.selectedP2))

# Select difficulty of player1. Can set as AI or human player. 
# x 0 = easy, 1 = normal, 2 = hard, 3 = human
    def clickP1(self, x):
        self.selectedP1 = x
        for b in range(len(self.selection1)):
            if b == x:
                self.selection1[b].configure(relief =SUNKEN)
            else:
                self.selection1[b].configure(relief=RAISED)

    # Select difficulty of player2. Can set as AI or human player
    def clickP2(self, x):
        self.selectedP2 = x
        for b in range(len(self.selection2)):
            if b == x:
                self.selection2[b].configure(relief =SUNKEN)
            else:
                self.selection2[b].configure(relief=RAISED)