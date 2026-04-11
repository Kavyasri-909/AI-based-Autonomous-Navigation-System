class Memory:
    def __init__(self):
        self.visited = set()

    def update(self, pos):
        self.visited.add(pos)

    def has_visited(self, pos):
        return pos in self.visited