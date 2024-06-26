import sys # Needed for exit
import copy
from Board import Board # Using the Board class form board.py
from Genetic import Genetic
from A_Star import AStar
from Fuzzy import FuzzyLogic
from datetime import datetime
import time

# 18-06-NR Creating Initial Promt
count = 0
user = input("\nDo you want to play X or O? X goes first. (X/O): ")
if user == 'X':
    computer = 'O'
    count = 1
elif user == 'O':
    computer = 'X'
else:
    print("\nInvalid Input\n")
    sys.exit()

print("\nChoose Preffered Mode:")
print("1) Minimax Algortihm with Alpha Beta Pruning + Fuzzy Logic for selecting depth")
print("2) Genetic Algorithm + A Star Algorithm")
mode = int(input("\nEnter The Preffered Mode: "))
if(mode > 2 or mode <=0):
    print("\nInvalid Input\n")
    sys.exit()

game = Board()
# 26-06-Tamim Remove Middle Elements
game.remove(4,4)
game.remove(4,5)
# 26-06-Tamim Remove Middle Elements End
print()
game.print()
# 18-06-NR Creating Initial Promt End

if(mode == 1):
    # 30-06-NR Creating Game Calculations
    while True:
        # computer's turn
        if count%2 == 0:
            moves = game.listMoves(computer)
            # check if game is over
            if len(moves) == 0:
                print("\nPlayer Won\n")
                exit()        
            print("\nComputer's Turn: ", end = " ")
            depth = 0
            bestVal = - sys.maxsize
            start_time = time.time()
            for move in moves:
                alpha = -1000
                beta = 1000
                temp = copy.deepcopy(game)
                temp.move(move[0][0], move[0][1], move[1][0], move[1][1])
                now = datetime.now()
                seconds = now.second
                milliseconds = now.microsecond // 1000  # converting microseconds to milliseconds
                fuzzy_logic = FuzzyLogic()
                new_cog = int(fuzzy_logic.compute_new_cog(seconds, milliseconds))
                depth = new_cog % 2
                depth = depth + 4
                cbv = Board.minimax(temp, computer, depth, alpha, beta)       
                if cbv > bestVal:
                    bestVal = cbv
                    bestMove = move
            end_time = time.time()
            time_difference = end_time - start_time
            print("Move " + str(bestMove[0]) + " to " + str(bestMove[1]) + " with depth: " + str(depth) + " with process time: {:.2f} ms\n".format(time_difference * 1000))
            game.move(bestMove[0][0], bestMove[0][1], bestMove[1][0], bestMove[1][1])   
        # player's turn
        else:
            moves = game.listMoves(user)
            # check if game is over
            if len(moves) == 0:
                print("\nComputer Won\n")
                exit()
            print("\nUser's Turn\n")
            # print all the available moves
            print("Available moves:")
            for i in range(len(moves)):
                print(str(i+1) + ") Move " + str(moves[i][0]) + " to " + str(moves[i][1]))
            move = int(input("\nEnter the number of the move that you want to make: ")) - 1
            print()
            if(move + 1 > len(moves) or move + 1 <= 0):
                print("\nInvalid Input\n")
                sys.exit()
            game.move(moves[move][0][0], moves[move][0][1], moves[move][1][0], moves[move][1][1])
        game.print()
        count += 1
        # 30-06-NR Ending Game Calculations

elif(mode == 2):
    # 30-06-NR Creating Game Calculations
    while True:
        # computer's turn
        if count%2 == 0:
            moves = game.listMoves(computer)
            # check if game is over
            if len(moves) == 0:
                print("\nPlayer Won\n")
                exit()        
            print("\nComputer's Turn: ", end = " ")
            heuristic_matrix = []
            matrix_row = []
            for i in range(9):
                ans = Genetic.main()
                matrix_row.append(ans)
                if(i+1)%3==0:
                    heuristic_matrix.append(matrix_row)
                    matrix_row = []
            astar = AStar()
            cost = astar.find_path_cost(heuristic_matrix)
            cost = cost % len(moves)
            bestMove = moves[cost]
            print("Move " + str(bestMove[0]) + " to " + str(bestMove[1]))
            game.move(bestMove[0][0], bestMove[0][1], bestMove[1][0], bestMove[1][1])   
        # player's turn
        else:
            moves = game.listMoves(user)
            # check if game is over
            if len(moves) == 0:
                print("\nComputer Won\n")
                exit()
            print("\nUser's Turn\n")
            # print all the available moves
            print("Available moves:")
            for i in range(len(moves)):
                print(str(i+1) + ") Move " + str(moves[i][0]) + " to " + str(moves[i][1]))
            move = int(input("\nEnter the number of the move that you want to make: ")) - 1
            if(move + 1 > len(moves) or move + 1 <= 0):
                print("\nInvalid Input\n")
                sys.exit()
            game.move(moves[move][0][0], moves[move][0][1], moves[move][1][0], moves[move][1][1])
        print()
        game.print()
        count += 1
        # 30-06-NR Ending Game Calculations
