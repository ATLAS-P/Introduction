

# Tic-Tac-Toe

CROSS = "X"
CIRCLE = "O"

def make_grid():
    return list(range(1, 10))

def print_start():
    print("Welcome to tic-tac-toe!!!!")

def print_end():
    pass

def three_horizontal(grid, player):
    pass

def three_vertical(grid, player):
    pass

def three_diagonal(grid, player):
    pass

def is_win(grid, player):
    return (three_vertical(grid, player) or
            three_horizontal(grid, player) or
            three_diagonal(grid, player))

def is_tie(grid):
    # all locations filled
    return False

def draw_grid(grid):
    for i in range(0,9,3):
        print(str(grid[i]) + "|" + str(grid[i + 1]) + "|" + str(grid[i + 2]))
        if i < 6:
            print("-----")

    print("")

def input_step(player, board):
    location = int(input("Where do you want to put your token? "))
    if location < 1 or location > 9: # if location is empty
        print("Your input was not valid!")
        input_step(player, board)
    else:
        set_board_value(board, player, location - 1)

def set_board_value(board, value, index):
    board[index] = value

def change_players(player):
    if player == CROSS:
        return CIRCLE
    else:
        return CROSS


grid = make_grid()
current_player = CROSS
print_start()

while not (is_win(grid, change_players(current_player)) or is_tie(grid)):
    draw_grid(grid)
    input_step(current_player, grid)
    current_player = change_players(current_player)

# draw the grid
# print ending message
