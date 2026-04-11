def create_grid(rows):
    return [[0 for _ in range(rows)] for _ in range(rows)]

def toggle_obstacle(grid, row, col):
    grid[row][col] = 1 if grid[row][col] == 0 else 0