from Ai import Ai
from ScoreFrame import ScoreFrame
class Controller(object):

# Set up a 8x8 board of zeroes (empty spots) ones(black bricks) and twos (white bricks)
# AIs set to None (Human controllers) at start
    def __init__(self):
        self.empty = 0
        self.player = 1
        self.opponent = 2
        self.ais = [None, None]  
        self.buttons = [[0 for _ in range(8)]for _ in range(8)]
        self.reset_board()

    def reset_board(self):
        self.whiteCount = 2
        self.blackCount = 2
        self.emptyCount = 60
        for x in range(8):
            for y in range(8):
                self.buttons[x][y] = 0
        self.buttons[3][3] = 2
        self.buttons[4][4] = 2
        self.buttons[3][4] = 1
        self.buttons[4][3] = 1
        self.player = 1
        self.opponent = 2

    # Reset the board to starting positions. 
    #Set AIs as selected by the player in playerSelectUI. Start the first move    
    # p1 and p2 are ints
    def restart_game(self):
        self.reset_board()
        self.game.reset_board()
        self.ais = [None, None]    
        self.update_texts(2, 2, 60)
        self.update_status("First turn: black player")
        #self.reset_click()
        ##self.ais= [self.get_AI_level_or_human(p1), self.get_AI_level_or_human(p2)]
        #self.update_status("First turn: player "+ self.first_player())
        ##self.next_move()
    # 0 returns easiest AI, 1 normal AI, 2 hard AI.
    # 3 returns None which sets player as human
    # x is an int

    def start_game(self,p1,p2):
        self.ais= [self.get_AI_level_or_human(p1), self.get_AI_level_or_human(p2)]
        #self.update_status("First turn: player "+ self.first_player())
        self.next_move()


      # 0 returns easiest AI, 1 normal AI, 2 hard AI, 3 minimax AI
    # 4 returns None which sets player as human
    # x is an int
    def get_AI_level_or_human(self, x):
        if x == 4:
            return None
        else:
            return Ai(x)

    # Check if player has a move to perform, if not switch player.
    # If that player doesn't have any legal moves either -> end game
    # If one of the players has a move to perform,
    # do the AIs move, or wait for player to click a move
    def next_move(self):
        if len(self.find_all_legal_moves()) == 0:
            self.update_status(self.get_player_color() + " has no legal moves, switching player")
            self.switch_player()
            if len(self.find_all_legal_moves()) == 0:
                self.update_status("No more legal moves, ending game. " + self.get_winner())
                return None

        if self.emptyCount == 0:
            self.update_status("No more empty squares, ending game. " + self.get_winner())
        else:
            if self.ais[self.player-1] != None:
                self.game.root.after(100,self.ai_move)

    # Get all legal moves and have the AI determine which move to make
    # Flip those bricks
    def ai_move(self):
        toFlip = self.ais[self.player-1].make_move(self.find_all_legal_moves())
        self.perform_move(toFlip)

    # Check every square on the board to see if a brick can be placed there.
    # Return a list of squares which are legal
    # and which bricks will be turned if you place brick there
    def find_all_legal_moves(self):
        legal = []
        lega = []
        for x in range(8):
            for y in range(8):
                lega = self.check_if_legal(x, y)
                if len(lega) > 0:
                    legal.append(lega)

        return legal

    # Called from the GameButtons when a player clicks. 
    # Check if player can place brick at that square, and perform the turn
    # x and y are ints
    def click(self, x, y):
        toTurn = self.check_if_legal(x,y)
        if len(toTurn) > 0:
            self.perform_move(toTurn)
        else: self.update_status("That's not a legal move, try again. Turn : " + self.get_player_color()+ " player")

    # check if current player is white or black
    def get_player_color(self):
        if self.player == 2:
            return "white"
        else: return "black"
    
    # If current player is black, change to white. Else change to black.
    def switch_player(self):
        self.opponent = self.player
        if self.player == 1:
            self.player = 2
        else: self.player = 1
        self.update_status("Turn: " + self.get_player_color()+" player ")

    # Update scoreboard. If the move placed 5 white bricks on the board
    # then black must have lost 4 and "empty" lost one.
    # x is int and represents how many bricks were altered
    def update_count(self, x):
        if self.player == 2:
            self.whiteCount += x
            self.blackCount -= x-1
        else:
            self.whiteCount -= x-1
            self.blackCount += x
        self.emptyCount -= 1
        self.game.update_texts(self.whiteCount, self.blackCount, self.emptyCount)

    # After move has been selected update gameboard and graphics to reflect changes.
    # Swap current player and opponent
    # Prepare for next move.
    # toTurn is a list of squares to turn
    def perform_move(self, toTurn):
        self.flip_buttons(toTurn)
        self.update_count(len(toTurn))
        self.switch_player()
        self.next_move()

    # Look at one particular square and see if current player can place a brick there.
    # If yes, return a list of squares that now will get players color
    def check_if_legal(self,x,y):
        toTurn = []
        if self.buttons[x][y] == self.empty:
            for i in range(9):
                if i == 4:
                    continue
                toTurnDir = self.check_direction(x,y,self.get_Y_direction(i), self.get_X_direction(i))
                if toTurnDir != None:
                    toTurn += toTurnDir

            if len(toTurn) > 0:
                    toTurn.append([x, y])

        return toTurn  

    # Change values in the gameboard and change the graphics for those squares
    def flip_buttons(self, toTurn):
        for brick in toTurn:
            self.buttons[brick[0]][brick[1]] = self.player
            self.game.change_color(brick[0], brick[1],self.get_player_color())

    # Get direction to move along the Y axis(rows), -1:up, 0:no movement, 1:up     
    def get_Y_direction(self,y):
        dirX = y % 3 - 1
        return dirX

    # Get direction to move along X axis (column), -1:left, 0:no movement, 1:right
    def get_X_direction(self, x):
        dirY = x // 3 - 1
        return dirY

    # Check that square being clicked is next to an opponent.
    # Keep checking that direction as long as there's an opponent
    # If you run outside the board or hit an empty square:
    # return None indicating no bricks will be turned in that direction
    # If you find a brick of your own color after finding an opponent then direction is legal.
    # Return list of squares that will be turned
    def check_direction(self, x, y, dirX, dirY):
        toTurn = []
        if x+dirX > 7 or x + dirX < 0 or y + dirY < 0 or y + dirY > 7:
            return None
        if self.buttons[x+dirX][y+dirY] == self.opponent:
            toTurn.append([x+dirX, y+dirY])
            for i in range(2,8):
                if x + dirX * i > 7 or x + dirX*i < 0 or y + dirY*i < 0 or y + dirY*i > 7:
                    return None
                if self.buttons[x+dirX*i][y+dirY*i] == self.opponent:
                    toTurn.append([x+dirX*i, y+dirY*i])
                if self.buttons[x+dirX*i][y+dirY*i] == self.empty:
                    return None
                if self.buttons[x+dirX*i][y+dirY*i] == self.player:
                    return toTurn

    #def first_status(self,text):
     #   self.game.scoreFrame.update_status(text)

    def update_status(self, text):
        self.game.scoreFrame.update_status(text)
    
    def update_texts(self, white,black, empty):
        self.game.scoreFrame.update_texts(white,black,empty)

    def get_winner(self):
        if self.whiteCount > self.blackCount:
            return "White player wins!"
        if self.blackCount > self.whiteCount:
            return "Black player wins!"
        return "The game ends in a tie"

    #def reset_click(self):
    #    self.game.playerSelect.reset_click()