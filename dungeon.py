from dungeon_gen import DungeonGen
from random import randrange
from math import sin, cos, radians


class Cell:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.char = '#'
        self.objects = []
        self.walkable = None
        self.already_seen = False

    def __repr__(self):
        return self.char


class Dungeon:
    def __init__(self, width, height):
        '''Initialize an empty dungeon'''
        self.width, self.height = width, height
        self.cells = [[Cell(x, y) for x in range(self.width)]
                      for y in range(self.height)]
        self.up_stair = None
        self.down_stair = None

    def cell(self, x, y):
        if not (0 <= x < self.width and 0 <= y < self.height):
            raise IndexError('Coordinates are out of range')
        return self.cells[y][x]

    def random_pos(self):
        '''Return random coordinates of a walkable cell'''
        while True:
            x, y = randrange(self.width), randrange(self.height)
            if self.cell(x, y).walkable:
                return x, y

    def populate(self):
        '''Add objects to the dungeon'''
        self.up_stair = self.random_pos()
        self.cell(*self.up_stair).char = '<'
        self.down_stair = self.random_pos()
        self.cell(*self.down_stair).char = '>'

    def generate(self):
        dungeon = DungeonGen(self.width, self.height)
        dungeon.generate(10)  # 10 rooms

        for y in range(self.height):
            for x in range(self.width):
                if dungeon.cells[y][x]:
                    self.cell(x, y).walkable = True
                    self.cell(x, y).char = '.'
                else:
                    self.cell(x, y).walkable = False
                    self.cell(x, y).char = '#'

        self.populate()

    def calc_fov(self, player):
        '''Return a matrix representing the Field Of Vision'''
        fov = []  # Create the fov matrix
        for y in range(self.height):
            fov.append([False] * self.width)

        for i in range(360):  # 0 -> 360 degrees
            ax = sin(radians(i))  # sin and cos take only radians
            ay = cos(radians(i))

            x = player.x
            y = player.y

            for z in range(3):  # The depth of the ray
                x += ax
                y += ay

                round_x, round_y = round(x), round(y)
                fov[round_y][round_x] = True
                self.cell(round_x, round_y).already_seen = True

                if not self.cell(round_x, round_y).walkable:  # The ray hits something
                    break

        return fov
