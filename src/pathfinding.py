import heapq

def heuristic(a, b):
    # Manhattan distance
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def astar(grid, start, goal):
    rows = len(grid)
    cols = len(grid[0])

    open_set = []
    heapq.heappush(open_set, (0, start))

    came_from = {}

    g_score = { (r, c): float("inf") for r in range(rows) for c in range(cols) }
    g_score[start] = 0

    f_score = { (r, c): float("inf") for r in range(rows) for c in range(cols) }
    f_score[start] = heuristic(start, goal)

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            return reconstruct_path(came_from, current)

        neighbors = get_neighbors(current, grid)

        for neighbor in neighbors:
            tentative_g = g_score[current] + 1

            if tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score[neighbor] = tentative_g + heuristic(neighbor, goal)

                heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return []  # no path


def get_neighbors(node, grid):
    row, col = node
    neighbors = []

    directions = [
        (1, 0), (-1, 0),
        (0, 1), (0, -1)
    ]

    for dr, dc in directions:
        r = row + dr
        c = col + dc

        if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
            if grid[r][c] == 0:  # ONLY walkable
                neighbors.append((r, c))

    return neighbors


def reconstruct_path(came_from, current):
    path = []
    while current in came_from:
        path.append(current)
        current = came_from[current]

    path.reverse()
    return path