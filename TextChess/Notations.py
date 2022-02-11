#!/usr/bin/env python
# coding: utf-8

# In[1]:


import chess
import chess.engine

board = chess.Board()
engine = chess.engine.SimpleEngine.popen_uci(r"C:\Users\leongezh\Desktop\Stuff\stockfish_14.1_win_x64_avx2\stockfish_14.1_win_x64_avx2.exe")
depth = 2


# In[2]:


def print_help():
   print ("Welcome to terminal chess, where you can play chess using only notations on your terminal \n   IN GAME COMMANDS\n   -board: show board\n   -undo: undo previous move\n   -newgame: start a new game\n   -best: let the engine suggest the best move\n   -score: display current score \n   -difficulty: show current difficulty (easy/medium/hard)\n   -empty: print an empty chessboard \n   -help: display list of commands")


# In[3]:


def empty():
    print("\n8 |_|#|_|#|_|#|_|#|\n\
7 |#|_|#|_|#|_|#|_|\n\
6 |_|#|_|#|_|#|_|#|\n\
5 |#|_|#|_|#|_|#|_|\n\
4 |_|#|_|#|_|#|_|#|\n\
3 |#|_|#|_|#|_|#|_|\n\
2 |_|#|_|#|_|#|_|#|\n\
1 |#|_|#|_|#|_|#|_|\n\
   a b c d e f g h\n\
          ")


# In[4]:


def change_dif(dif):
    if dif == "easy":
        depth = 2
    elif dif == "medium":
        depth = 5
    elif dif == "hard":
        depth = 10
    else:
        print("Please input a proper difficulty (easy/medium/hard)")


# In[5]:


def human_move(san_notation):
    if san_notation == "undo":
        board.pop()
    elif san_notation == "newgame":
        game_start()
    elif san_notation == "board":
        print(board)
    elif san_notation == "empty":
        empty()
    elif san_notation == "help":
        print_help()
    elif san_notation == "difficulty":
        change_dif(input("Change difficulty to: "))
    else:    
        try:
            move = board.parse_san(san_notation)
        except ValueError:
            print("Sorry I didn't get what you meant")
            return
        
        if not move in board.legal_moves:
            print("Please make a legal move!")
            return
        else:
            board.push(move)
            engine_move()
            return


# In[6]:


def engine_move():
    result = engine.play(board, chess.engine.Limit(depth=depth))
    print("Computer: "+ board.san(result.move))
    board.push(result.move)
    return


# In[7]:


def game_start():
    user_colour = input("Please choose a colour (w/b): ")
    if (user_colour != 'w' and user_colour != 'b'):
        print("Please choose a proper colour (w/b)")
    if user_colour == 'b':
        engine_move()

    while not board.is_game_over():
        user_input = input("Your move: ")
        human_move(user_input)
    board.outcome()
    board.reset()


# In[ ]:


print("Welcome to terminal chess")
user_start = input("Type ""start"" to begin or ""help"" for list of commands: ")

while(True):
    if user_start == "start":
        game_start()
        user_start = ""
    elif user_start == "help":
        print_help()
        user_start = ""
    else:
        user_start = input("Type ""start"" to begin or ""help"" for list of commands: ")
    


# In[ ]:





# In[ ]:




