from game_logic import make_move
import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")


def parse_input(user_move): # parsing a moves on the board
    if not isinstance(user_move, str):
        return None
    user_move = user_move.strip().upper()
    if len(user_move) != 2:
        return None
    
    col_char = user_move[0]
    row_char = user_move[1]
  
    if row_char not in "12345" or col_char not in "ABCDE":
        return None
    try:
        row = int(row_char) - 1
        col = ord(col_char) - ord("A")
        return row , col
    except Exception:
        return None
    

