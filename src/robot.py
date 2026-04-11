import pygame

class Robot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.path_index = 0

    def follow_path(self, path):
        if self.path_index < len(path):
            self.x, self.y = path[self.path_index]
            self.path_index += 1

    def draw(self, win, cell_size):
        pygame.draw.rect(
            win,
            (0, 255, 0),
            (self.y * cell_size, self.x * cell_size, cell_size, cell_size)
        )