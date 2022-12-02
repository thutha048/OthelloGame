import random as ran
from GameFrame import GameFrame
class Ai(object):

    def __init__(self, difficulty):
        '''
        Constructor
        '''
        self.difficulty = difficulty 
    # Select a move from the list of legal moves, based on what difficulty AI is in use.    
    def make_move(self, possibleMoves):
        if self.difficulty == 0:
            return self.random_move(possibleMoves)
        if self.difficulty == 1:
            return self.greedy(possibleMoves)
        if self.difficulty == 2:
            return self.hard(possibleMoves)
        if self.difficulty==3:
            return self.minimax(possibleMoves)

    # Select a random move out of the legal ones.
    # Known as "easy" difficulty
    def random_move(self, possibleMoves):
        select =  ran.randrange(len(possibleMoves))
        return possibleMoves[select]

    # Check the list of legal moves and select the one that will turn the most bricks.
    # If several moves turns the same amount of bricks, return a random one of them
    # Known as "normal" difficulty
    def greedy(self, possibleMoves):
        biggest = 0
        greediestMoves = []
        for x in range(len(possibleMoves)):
            if len(possibleMoves[x]) == biggest:
                greediestMoves.append(possibleMoves[x])
            if len(possibleMoves[x]) > biggest:
                biggest = len(possibleMoves[x])
                greediestMoves = []
                greediestMoves.append(possibleMoves[x])

        select =  ran.randrange(len(greediestMoves))
        return greediestMoves[select]

    # Values indicating how "good" a square is to have, used only by the hardest AI
    square_values = [ 
            [99,  -8,   8,  6,  6,  8,  -8, 99], 
            [-8, -24,  -4, -3, -3, -4, -24, -8],  
            [8,   -4,   7,  4,  4,  7,  -4,  8], 
            [6,   -3,   4,  0,  0,  4,  -3,  6],  
            [6,   -3,   4,  0,  0,  4,  -3,  6],
            [8,   -4,   7,  4,  4,  7,  -4,  8],
            [-8, -24,  -4, -3, -3, -4, -24, -8],
            [99,  -8,   8,  6,  6,  8,  -8, 99] 
        ]

    # Go trough the list of legal moves to find the move that adds the most "value" based on the valuegrid.
    # If several moves add the same "value", randomly return one of them 
    # Known as "hard" difficulty
    def hard(self, possibleMoves):
       # print("posslist= ",possibleMoves)
        best = -99
        bestMoves = [] #list
        for x in range(len(possibleMoves)):
            #print("x= ",x)
            #print ("possi= ", possibleMoves[x][-1][0])
            #print("poss[x]=",possibleMoves[x])
            #print("poss[x][-1]=",possibleMoves[x][-1])
            #print("poss[x][0]=",possibleMoves[x][0])

            value = self.square_values[possibleMoves[x][-1][0]][possibleMoves[x][-1][1]]
            #print("value= ",value)

            if value == best:
                bestMoves.append(possibleMoves[x])
                best = value
            if value > best:
                bestMoves = [possibleMoves[x]]
                best = value
        select =ran.randrange(len(bestMoves))
        return bestMoves[select]

    def _str_(self):
        return "hard"

  
    def minimax(self,possibleMoves):
    
        def _init_(self,turn, depth):
            super()._init_(turn)
            self.depth = depth
        
        def eval_board(board,turn):
            tmp_board = board.get_board()
            total=0
            for x in range(8):
                for y in range(8):
                    if tmp_board[x][y] == self.turn:
                        total+= self.square_values[x][y]
                    if tmp_board[x][y]== 3- self.turn:
                        total -= self.square_values[x][y]
            return total

        def minimaxRoot(self,depth,game, maxPlayer):
            newMoves = []
            bestMoves = -9999

            for x in range(len(possibleMoves)):
                newMoves.append(possibleMoves[x][-1])
            
            for i in range(len(newMoves)):
                newGameMove = newMoves[i]
                game.make_move(newGameMove)
                value = minimax1(depth-1,game, 3-maxPlayer)
                
                if value >= bestMoves:
                    bestMoves=value
                    bestMoveFound = newGameMove

            return bestMoveFound


        def minimax1(depth,game, maxPlayer):
            if depth ==0 or len(possibleMoves) ==0:
                return self.eval_board(game,maxPlayer)
            
            newMoves =[]
            for x in range(len(possibleMoves)):
                newMoves.append(possibleMoves[x][-1])

            if maxPlayer :
                bestMove = -9999
                for i in range(len(possibleMoves)):
                    game.possibleMoves(newMoves[i])
                    bestMove = max (bestMove, minimax1(depth-1,game,3-maxPlayer))
                    #game.undo()?
                return bestMove
            else:
                bestMove =9999
                for i in range(len(possibleMoves)):
                    game.make_move(newMoves[i])
                    bestMove = min (bestMove, minimax1(depth-1,game,3-maxPlayer))
                return bestMove
        
               

'''
    def mini(self,possibleMoves):
        def _init_(self, depth):
            self.depth = depth
        
        def processmimax(depth,maxPlayer):
            if depth==0 :
                return self.hard(possibleMoves)
            
            newMoves = []
            for i in range(len(possibleMoves)):
                newMoves.append(possibleMoves[i])
            #gan newMove= possibleMoves cua AI

            if maxPlayer:
                bestMove = -9999
                for i in range(len(newMoves)):
                    possi(newMoves[i][-1])
                    #possi : func find possible move of AI newMoves[x][-1]
                    bestMove= max(bestMove,processmimax(depth-1,3-maxPlayer))
                return bestMove    
          '''      

