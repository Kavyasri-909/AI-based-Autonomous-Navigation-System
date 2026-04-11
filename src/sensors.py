def get_neighbors(grid, pos):
    rows, cols = len(grid), len(grid[0])
    r, c = pos

    neighbors = []
    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            neighbors.append((nr, nc, grid[nr][nc]))

    return neighbors