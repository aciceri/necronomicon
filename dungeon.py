from bsp_dungeon import BspDungeon


class Cell:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.char = '#'
        self.objects = []
        self.walkable = None

    def __repr__(self):
        return self.char


class Dungeon:
    def __init__(self, width, height):
        '''Initialize an empty dungeon'''
        self.width, self.height = width, height
        self.cells = [[Cell(x, y) for x in range(self.width)]
                      for y in range(self.height)]

    def cell(self, x, y):
        if not (0 <= x < self.width and 0 <= y < self.height):
            raise IndexError('Coordinates are out of range')
        return self.cells[y][x]

    def generate(self, depth):
        bsp_dungeon = BspDungeon(self.width, self.height)
        bsp_dungeon.generate(depth)

        for y in range(self.height):
            for x in range(self.width):
                if bsp_dungeon.cells[y][x]:
                    self.cells[y][x].walkable = True
                    self.cells[y][x].char = '.'
                else:
                    self.cells[y][x].walkable = False
                    self.cells[y][x].char = '#'
