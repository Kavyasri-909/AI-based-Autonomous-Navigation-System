import sys
import os
sys.path.append(os.path.dirname(__file__))

import pygame
from grid import create_grid, toggle_obstacle
from robot import Robot
from pathfinding import astar

# ------------------ SETTINGS ------------------
WIDTH = 600
ROWS = 20
CELL_SIZE = WIDTH // ROWS

WHITE = (255, 255, 255)
GRAY = (200, 200, 200)

# ------------------ DRAW GRID ------------------
def draw_grid_lines(win):
    for i in range(ROWS):
        pygame.draw.line(win, GRAY, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE))
        pygame.draw.line(win, GRAY, (i * CELL_SIZE, 0), (i * CELL_SIZE, WIDTH))

# ------------------ MAIN ------------------
def main():
    pygame.init()
    win = pygame.display.set_mode((WIDTH, WIDTH))
    pygame.display.set_caption("AI Autonomous Navigation")

    grid = create_grid(ROWS)

    robot = Robot(0, 0)
    goal = (ROWS - 1, ROWS - 1)

    path = []

    running = True
    clock = pygame.time.Clock()

    while running:
        clock.tick(10)
        win.fill(WHITE)

        # EVENTS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # LEFT CLICK → place obstacle
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                row = pos[1] // CELL_SIZE
                col = pos[0] // CELL_SIZE
                toggle_obstacle(grid, row, col)

            # RIGHT CLICK → remove obstacle
            if pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                row = pos[1] // CELL_SIZE
                col = pos[0] // CELL_SIZE
                grid[row][col] = 0

            # PRESS SPACE → compute path
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    path = astar(grid, (robot.x, robot.y), goal)

        # MOVE ROBOT
        if path:
            robot.follow_path(path)

        # DRAW EVERYTHING
        for row in range(ROWS):
            for col in range(ROWS):
                if grid[row][col] == 1:
                    pygame.draw.rect(
                        win, (0, 0, 0),
                        (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                    )

        # Draw goal (blue)
        pygame.draw.rect(
            win, (0, 0, 255),
            (goal[1] * CELL_SIZE, goal[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        )

        # Draw robot (green)
        robot.draw(win, CELL_SIZE)

        draw_grid_lines(win)
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()