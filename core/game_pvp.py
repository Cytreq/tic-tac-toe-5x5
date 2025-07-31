from game_logic import switch_player, make_move,is_move_valid, check_draw, check_win
from helpers import parse_input
from board import print_board, game_board

def move_input():
     user_move = input("Enter your move: ")
     return user_move

def play_pvp(): # start to play pvp mode
    print("Starting PvP mode...")
    current_player = "X"
    while True: 
        print_board(game_board)
        user_move = move_input()
        parsed = parse_input(user_move)
        if parsed == None:
            input("Wrong format of input, press Enter to continue: ")
            continue
        row, col = parsed
        if not is_move_valid(row, col):
            input("Move is not valid, press Enter to try again: ")
            continue
        make_move(row, col, current_player)
        if check_win(current_player):
            print_board(game_board)
            print(f"Player {current_player} won the game! Congrats!")
            break
        if check_draw():  # check for draw
           print("It's a draw, Game over!")
           break
        current_player = switch_player(current_player)

