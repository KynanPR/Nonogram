import sys, pygame, random
pygame.init()

cell_states = (0, 1, 2)
cell_empty = cell_states[0]
cell_blocked = cell_states[1]
cell_filled = cell_states[2]


width, height = 5, 5

play_grid = []
solution_grid = []

def row(row_number):
    index = row_number - 1
    return index

def column(column_number):
    index = column_number - 1
    return index

def init_play_grid():
    global play_grid
    # Create array of arrays
    play_grid = [
        [cell_empty for i in range(width)] for j in range(height) # Each array is a column
        ]
    print("Initialised play grid with size", width, "x", height)
    
def init_solution_grid():
    global solution_grid
    # Create random solution grid
    solution_grid = [
        [random.randint(1, 2) for i in range(width)] for j in range(height) # Each array is a column
        ]
    print("Initialised solution grid with size", width, "x", height)


key_top = [0 for i in range(width)]
key_side = [[0] * height]

def generate_keys():
    global key_top, key_side


for x in range(width):
    for y in range(height):
        state = solution_grid[x][y]
        if state == cell_filled:
            key_top[x] += 1




init_play_grid()
init_solution_grid()
#print("Play grid:", play_grid, "Solution grid:", solution_grid)