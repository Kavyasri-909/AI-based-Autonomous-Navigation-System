import heapq

def astar(grid, start, goal):
    rows = len(grid)

    def heuristic(a, b):
        # Manhattan distance
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    open_set = []
    heapq.heappush(open_set, (0, start))

    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}

    while open_set:
        current = heapq.heappop(open_set)[1]

        if current == goal:
            # reconstruct path
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.reverse()
            return path

        x, y = current

        neighbors = [
            (x+1, y),
            (x-1, y),
            (x, y+1),
            (x, y-1)
        ]

        for nx, ny in neighbors:
            if 0 <= nx < rows and 0 <= ny < rows:
                if grid[nx][ny] == 1:
                    continue  # obstacle

                tentative_g = g_score[current] + 1

                if (nx, ny) not in g_score or tentative_g < g_score[(nx, ny)]:
                    came_from[(nx, ny)] = current
                    g_score[(nx, ny)] = tentative_g
                    f_score[(nx, ny)] = tentative_g + heuristic((nx, ny), goal)

                    heapq.heappush(open_set, (f_score[(nx, ny)], (nx, ny)))
    return []  # no path found