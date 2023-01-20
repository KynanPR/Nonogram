import random

width, height = 5, 5


solution_grid = []

def init_solution_grid():
    global solution_grid
    # Create random solution grid
    solution_grid = [
        [random.randint(1, 2) for i in range(width)] for j in range(height) # Each array is a column
        ]
    print("Initialised solution grid with size", width, "column", height)

key_top = [[] for i in range(width)]

init_solution_grid()

print(solution_grid)

for column in range(width):
    block = 0 # Reset block counter for new column
    in_block = False
    for row in range(height):
        state = solution_grid[column][row]
        if state == 2: # When cell is filled
            if not is_in_block:
                
            key_top[column][block] += 1
            is_in_block = True
        elif is_in_block: # When cell is blocked
            block += 1
            is_in_block = False
print("Key", key_top)