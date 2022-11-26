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

    #def animate_flip():
    #def change_icon():

    def draw_cell(self, row: int, col: int) -> None:
        ''' Draws the specified cell '''
        self.create_oval(col * self.get_cell_width(),
                                row * self.get_cell_height(),
                                (col + 1) * self.get_cell_width(),
                                (row + 1) * self.get_cell_height()
                               )                         

    def get_cell_width(self) -> float:
        ''' Returns a game cell's width '''
        return 600 / self.get_columns()

    def get_cell_height(self) -> float:
        ''' Returns a game cell's height '''
        return 750 / self.get_rows()

    def get_board_width(self) -> float:
        ''' Returns the board canvas's width '''
        return float(self._board.winfo_width())

    def get_board_height(self) -> float:
        ''' Returns the board canvas's height '''
        return float(self._board.winfo_height())