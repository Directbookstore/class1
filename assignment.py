def count_adjacent_mines(grid):
    # Define the dimensions of the grid
    rows = len(grid)
    cols = len(grid[0])
    
    # Create a copy of the grid to store the result
    result_grid = [[0] * cols for _ in range(rows)]
    
    # Define directions for all 8 possible adjacent cells (up, down, left, right, and diagonals)
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    
    # Iterate through each cell in the grid
    for row in range(rows):
        for col in range(cols):
            # Check if the current cell is a mine
            if grid[row][col] == '#':
                result_grid[row][col] = '#'
            else:
                # Count adjacent mines
                mine_count = 0
                for dr, dc in directions:
                    new_row, new_col = row + dr, col + dc
                    # Check if the adjacent cell is within bounds and is a mine
                    if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == '#':
                        mine_count += 1
                # Update the cell with the mine count
                result_grid[row][col] = str(mine_count)
    
    return result_grid

# Example input grid
input_grid = [
    ["-", "-", "-", "#", "#"],
    ["-", "#", "-", "-", "-"],
    ["-", "-", "#", "-", "-"],
    ["-", "#", "#", "-", "-"],
    ["-", "-", "-", "-", "-"]
]

# Run the function and print the result
output_grid = count_adjacent_mines(input_grid)
for row in output_grid:
    print(" ".join(row))

