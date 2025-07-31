game_board = [
[' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ']
]

def print_board(game_board): 
    print(" | A | B | C | D | E | \n----------------------") # these are collumns on the board
    for i, row in enumerate(reversed(game_board) , start=1):
        print(f"{6 - i}| {' | '.join(row)} |")
        print("----------------------")





