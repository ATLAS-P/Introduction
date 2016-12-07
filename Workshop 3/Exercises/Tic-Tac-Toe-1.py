

# Tic-Tac-Toe

CROSS = "X"
CIRCLE = "O"

def make_grid():
    return list(range(1, 10))

def print_start():
    print("Welcome to tic-tac-toe!!!!")

def print_end():
    pass

def is_win():
    return False

def is_tie():
    return False

def draw_grid(grid):
    print(grid)

def input_step():
    pass

def set_board_value():
    pass

def change_players():
    pass


grid = make_grid()
current = CROSS
print_start()

while not (is_win() or is_tie()):
    draw_grid(grid)
    # drawing the grid
    # ask for input and put on screen
    # change players

# draw the grid
# print ending message
