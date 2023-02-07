import random as ran
import copy
from GameFrame import GameFrame
from GameButtons import GameButtons
class Ai(object):

    def __init__(self, difficulty):
        self.depth =0
        self.difficulty = difficulty 
        self.board = GameButtons
    # Select a move from the list of legal moves, based on what difficulty AI is in use.    
    def make_move(self, possibleMoves,board):
        if self.difficulty == 0:
            return self.random_move(possibleMoves)
        if self.difficulty == 1:
            return self.greedy(possibleMoves)
        if self.difficulty == 2:
            return self.hard(possibleMoves)
        if self.difficulty==3:
            return self.hard(possibleMoves)

    # Select a random move out of the legal ones.
    # Known as "easy" difficulty
    def random_move(self, possibleMoves):
        select =  ran.randrange(len(possibleMoves))
        return possibleMoves[select]
    
    # def random_time(self, possibleMoves):
        # timeit.timeit(self.random_move(possibleMoves), number=1)
        # start_time=time.time()
        # self.random_move(possibleMoves)
        # end_time=time.time()
        # elapsed_time = end_time - start_time
        # print("Random - elapsed_time: {0}".format(elapsed_time)+"[sec]")
    


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
            [100,  -8,   8,  6,  6,  8,  -8, 100], 
            [-8, -24,  -4, -3, -3, -4, -24, -8],  
            [8,   -4,   7,  4,  4,  7,  -4,  8], 
            [6,   -3,   4,  0,  0,  4,  -3,  6],  
            [6,   -3,   4,  0,  0,  4,  -3,  6],
            [8,   -4,   7,  4,  4,  7,  -4,  8],
            [-8, -24,  -4, -3, -3, -4, -24, -8],
            [100,  -8,   8,  6,  6,  8,  -8, 100] 
        ]

    def hard(self, possibleMoves):
        #print("posslist= ",possibleMoves)
        best = -99
        bestMoves = [] #list
        for x in range(len(possibleMoves)):
            value = self.square_values[possibleMoves[x][-1][0]][possibleMoves[x][-1][1]]
            if value == best:
                bestMoves.append(possibleMoves[x])
                best = value
            if value > best:
                bestMoves = [possibleMoves[x]]
                best = value
        select =ran.randrange(len(bestMoves))
        return bestMoves[select]
        
#-------------------------------------
    def superhard(self, possibleMoves):
        min_eval_board=-9999
        max_eval_board=9999
            
        def eval_board(self,board,turn):
            tmp_board = board.get_board()
            total=0
            for x in range(8):
                for y in range(8):
                    if tmp_board[x][y] == self.turn:
                        total+= self.square_values[x][y]
                    if tmp_board[x][y]== 3- self.turn:
                        total -= self.square_values[x][y]
            return total

        def sort_nodes(self,moves):
            sorted_nodes=[[move, self.square_values[move[-1][0]][move[-1][1]]]for move in moves]
            sorted_nodes = sorted(sorted_nodes, key = lambda node: node[1], reverse = True)
            return [node[0] for node in sorted_nodes]

        def minimax_alpha_beta(self, board, depth, player, Alpha, Beta, turn,possibleMoves):
            valid_moves = possibleMoves
            best_value = 0

            if depth == 0 or len(valid_moves) == 0:
                return self.eval_board(board, turn)

            if player == turn:
                tiles = self.sort_nodes(valid_moves)
                best_value = self.min_eval_board

                for piece in tiles:
                    board_temp = copy.deepcopy(board)

                    board_temp.make_move(player, piece[0], piece[1]) 
                    val = self.minimax_alpha_beta(board_temp, depth - 1, 3 - player, Alpha, Beta, turn)
                    
                    #print(val, "Alpha_Beta_sorted() val maximize_player")

                    if val > best_value:
                        best_value = val

                    if val > Alpha:
                        Alpha = val

                    if Alpha >= Beta:
                        break #beta cut-off
                    
                #print(Alpha, "Alpha_Beta_sorted() Alpha maximize_player")
            else: # minimizingPlayer
                tiles = self.sort_nodes(valid_moves)
                best_value = self.max_eval_board
                for piece in tiles:
                    board_temp = copy.deepcopy(board)

                    board_temp.make_move(player, piece[0], piece[1])  
                    val = self.minimax_alpha_beta(board_temp, depth - 1, 3 - player, Alpha, Beta, turn)
                    
                    #print(val, "Alpha_Beta_sorted() val minimize_player")

                    if val < best_value:
                        best_value = val
                    
                    if val < Beta:
                        Beta = val

                    if Alpha >= Beta:
                        break #alpha cut-off

                #print(Beta, "Alpha_Beta_sorted() Beta minimize_player")
            
            #print(best_value, "Alpha_Beta_sorted()", depth)
            return best_value
        def superHard(self, possibleMoves,board):
            moves = possibleMoves
            sorted_tiles = self.sort_nodes(moves)

            max_points = self.min_eval_board
            best_move = []

            for move in sorted_tiles:
                board_temp = copy.deepcopy(board)
                board_temp.make_move(self.turn, move[0], move[1]) 

                points = self.minimax_alpha_beta(board_temp, self.depth, 3 - self.turn, max_points, self.max_eval_board, self.turn)
                        
                if points > max_points:
                    max_points = points
                    best_move = move
                elif points == max_points:
                    if ran.randint(0, 1):
                        best_move = move

            return best_move