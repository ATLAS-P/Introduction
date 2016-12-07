

# Tic-Tac-Toe

CROSS = "X"
CIRCLE = "O"

def make_grid():
    return list(range(1, 10))

def print_start():
    print("Welcome to tic-tac-toe!!!!")

def print_end(winner):
    print(winner, "was the winner!!!")

def three_horizontal(grid, player):
    for i in range(0,9,3):
        if grid[i] == player and grid[i + 1] == player and grid[i + 2] == player:
            return True

    return False

def three_vertical(grid, player):
    for i in range(3):
        if grid[i] == player and grid[i + 3] == player and grid[i + 6] == player:
            return True

    return False

def three_diagonal(grid, player):
    first_diagonal = grid[0] == player and grid[4] == player and grid[8] == player
    second_diagonal = grid[2] == player and grid[4] == player and grid[6] == player

    return first_diagonal or second_diagonal

def is_win(grid, player):
    return (three_vertical(grid, player) or
            three_horizontal(grid, player) or
            three_diagonal(grid, player))

def is_tie(grid):
    for i in grid:
        if i is not CROSS and i is not CIRCLE:
            return False

    return True

def draw_grid(grid):
    for i in range(0,9,3):
        print(str(grid[i]) + "|" + str(grid[i + 1]) + "|" + str(grid[i + 2]))
        if i < 6:
            print("-----")

    print("")

def is_empty(grid, location):
    if str(grid[location]) not in CROSS + CIRCLE:
        return True

    return False

def input_step(player, board):
    location = int(input("Where do you want to put your token? "))
    if location < 1 or location > 9 or not is_empty(grid, location - 1):
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

draw_grid(grid)
print_end(change_players(current_player))
