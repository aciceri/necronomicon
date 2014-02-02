class Cell:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.char = '#'
        self.objects = []

    def __repr__(self):
        return self.char


class Map:
    def __init__(self):
        '''Initialize an empty map'''
        self.cells = [Cell(x, y) for y in range(20) for x in range(80)]

    def cell(self, x, y):
        if not (0 <= x < 80 and 0 <= y < 20):
            raise IndexError('Coordinates are out of range')
        return self.cells[y * 80 + x]
