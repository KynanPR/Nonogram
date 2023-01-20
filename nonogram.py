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
        [cell_empty for i in range(height)] for j in range(width) # Each array is a column
        ]
    print("Initialised play grid with size", width, "x", height)
    
def init_solution_grid():
    global solution_grid
    # Create random solution grid
    solution_grid = [
        [random.randint(1, 2) for i in range(height)] for j in range(width) # Each array is a column
        ]
    print("Initialised solution grid with size", width, "x", height)


key_top = [[] for i in range(width)]
key_side = [[] for i in range(height)]

def generate_keys():
    global key_top, key_side


# # Iterate across columns and create key
# for column in range(width):
#     chunk = 0 # Reset chunk counter for new column
#     in_chunk = False # Reset chunk flag
    
#     # Iterate down column adding chunks and incrementing chunk lengths
#     for row in range(height):
#         state = solution_grid[column][row] # Get state of cell
        
#         if state == cell_filled:
#             if not in_chunk: # Detect start of chunk
#                 key_top[column].append(1) # Start counting chunk length
#                 in_chunk = True # Set flag to be in chunk
                
#             else: # Continuing chunk
#                 key_top[column][chunk] += 1
        
#         # Detect end of chunk and move onto next
#         elif in_chunk:
#             chunk += 1
#             in_chunk = False

# for row in range(height):
#     # Reset chunk counter and flag for new row
#     chunk = 0
#     in_chunk = False
    
#     # Iterate along row adding chunks and incrementing chunk lengths
#     for column in range(height):
#         state = solution_grid[column][row] # Get state of cell
        
#         if state == cell_filled:
#             if not in_chunk:
#                 key_side[row].append(1)
#                 in_chunk = True
                
#             else:
#                 key_side[row][chunk] += 1
        
#         elif in_chunk:
#             chunk += 1
#             in_chunk = False



 
 
def generate_keys():
    # Init vars
    column_index, row_index = 0, 0
    column = {
        "direction_primary": column_index,
        "direction_secondary": row_index,
        "dimension_primary": width, #2
        "dimension_secondary": height, #5
        "key_edge": key_top
        }

    row = {
        "direction_primary": row_index,
        "direction_secondary": column_index,
        "dimension_primary": height, #5
        "dimension_secondary": width, #2
        "key_edge": key_side
    }

    # Create column key, then row key
    for switch in (column, row):
                
        # Iterate along primary direction and create key
        for switch["direction_primary"] in range(switch["dimension_primary"]):
            
            # Reset chunk counter and flag for next column/row
            chunk = 0
            in_chunk = False
            active_key_part = switch["key_edge"][switch["direction_primary"]]
            
            # Iterate along secondary direction adding chunk and incrementing lengths
            for switch["direction_secondary"] in range(switch["dimension_secondary"]):
                # Get state of cell - need to rever order of array indicies for rows
                if switch == column:
                    state = solution_grid[switch["direction_primary"]][switch["direction_secondary"]]
                if switch == row:
                    state = solution_grid[switch["direction_secondary"]][switch["direction_primary"]]
                
                if state == cell_filled:
                    if not in_chunk: # Detect start of chunk
                        active_key_part.append(1) # Start counting chunk length
                        in_chunk = True # Set in chunk flag
                    
                    else: # Continuing chunk
                        active_key_part[chunk] += 1
                
                # Detect end of chunk and move onto next
                elif in_chunk:
                    chunk += 1
                    in_chunk = False
            if len(active_key_part) == 0:
                active_key_part.append(0)
                
        column_index, row_index = 0, 0 # Reset indicies
            
    
square_grid_size = int(input("Enter grid size you want...\n"))

width, height = square_grid_size, square_grid_size
         

init_play_grid()
init_solution_grid()
generate_keys()

#print("Play Grid:", play_grid, "\nSolution Grid:", solution_grid, "\nTop Key:", key_top, "\nSide Key:", key_side)

print("Top Key:", key_top, "\nSide Key:", key_side)