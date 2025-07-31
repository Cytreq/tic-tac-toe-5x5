from board import game_board

def is_move_valid(row, col): # check is the move is correct 
    if game_board[row][col] == ' ':
         return True
    else: 
         return False


def make_move(row, col, current_player): # printing the move to the board 
        game_board[row][col] = current_player

def switch_player(current_player): # swithing from player A to B and vice versa 
      if current_player == "X":
           return "O"
      else:
           return "X"
      
def check_win(current_player): # check for win 
    if check_win_row(current_player) or check_win_coll(current_player) or check_win_diagonal_right(current_player, win_length=4) or check_win_diagonal_left(current_player, win_length=4):
             return True
    else: 
         return False

def check_win_row(current_player):# checking the the win in row 1, 2 etc
     for _row in game_board:
          count = 0
          for _cell in _row:
               if _cell == current_player:
                    count += 1
                    if count == 4:
                         return True
               else:
                    count = 0              

def check_win_coll(current_player):
     for _col in range(len(game_board[0])):
          count = 0
          for _row in range(len(game_board)):
               if game_board[_row][_col]== current_player:
                    count += 1
                    if count == 4:
                         return True
               else:
                    count = 0

               ...

def check_win_diagonal_right(current_player, win_length=4):
    rows = len(game_board)
    cols = len(game_board[0])
    
    for row in range(rows - win_length + 1):
        for col in range(cols - win_length + 1):
            count = 0
            for i in range(win_length):
                if game_board[row + i][col + i] == current_player:
                    count += 1
                else:
                    break
            if count == win_length:
                return True
    return False

def check_win_diagonal_left(current_player, win_length=4): # I need to understand more how this diagonals check works
    rows = len(game_board)
    cols = len(game_board[0])
    
    for row in range(rows - win_length + 1):
        for col in range(win_length - 1, cols):
            count = 0
            for i in range(win_length):
                if game_board[row + i][col - i] == current_player:
                    count += 1
                else:
                    break
            if count == win_length:
                return True
    return False


def check_draw(): # return True is the board is full (draw) else it's returning False
    for one_row in game_board:
          for cell in one_row:
               if cell == ' ':
                    return False
    return True

         
    
