# tic-tac-toe

CROSS = "X"
CIRCLE = "O"

def create_board():
    return list(range(1, 10))

def starting_player():
    return CROSS

def starting_message():
    print("Welcome to Tic-Tac-Toe!")

def ending_message(winner):
    print(winner, "won!")

def has_won(board, player):
    return three_vertical(board, player) or three_horizontal(board, player) or three_diagonal(board, player)

def three_horizontal(board, player):
    for i in range(0, 9, 3):
        if board[i] == player and board[i + 1] == player and board[i + 2] == player:
            return True
    return False

def three_vertical(board, player):
    for i in range(3):
        if board[i] == player and board[i+3] == player and board[i+6] == player:
            return True
    return False

def three_diagonal(board, player):
    first = board[0] == player and board[4] == player and board[8] == player
    second = board[2] == player and board[4] == player and board[6] == player

    return first or second

def draw_board(board):
    for i in range(0, 9, 3):
        print(str(board[i]) + "|" + str(board[i + 1]) + "|" + str(board[i + 2]))
        if i != 6:
            print("-----")
    print()

def other_player(player):
    if player == CROSS:
        return CIRCLE
    else:
        return CROSS

def set_board_value(board, index, value):
    board[index] = value

def is_free(board, location):
    return str(board[location]) not in CROSS + CIRCLE

def move(board, player):
    location = int(input("Where do you want to place your token?\n")) - 1
    if not is_free(board, location):
        print("Already taken")
        move(board, player)
    else:
        set_board_value(board, location, player)

board = create_board()
current_player = starting_player()
starting_message()

while not has_won(board, other_player(current_player)):
    draw_board(board)
    move(board, current_player)
    current_player = other_player(current_player)

draw_board(board)
ending_message(other_player(current_player))





'''
Possible things left to do:

- what if there is a tie?
- computer ai (3 levels)
- more graphics
- ask if player wants to play again and restart game
etc.....
'''


