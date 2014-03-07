from procedural_dungeon import ProceduralDungeon
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

    def cell(self, x, y):
        if not (0 <= x < self.width and 0 <= y < self.height):
            raise IndexError('Coordinates are out of range')
        return self.cells[y][x]

    def random_pos(self):
        '''Return random coordinates of a walkable cell'''
        while True:
            x, y = randrange(self.width), randrange(self.height)
            if self.cells[y][x].walkable:
                return x, y

    def generate(self):
        proc_dungeon = ProceduralDungeon(self.width, self.height)
        proc_dungeon.generate(10)

        for y in range(self.height):
            for x in range(self.width):
                if proc_dungeon.cells[y][x]:
                    self.cells[y][x].walkable = True
                    self.cells[y][x].char = '.'
                else:
                    self.cells[y][x].walkable = False
                    self.cells[y][x].char = '#'

    def calc_fov(self, player_x, player_y):
        '''Return a matrix representing the Field Of Vision'''
        fov = []
        for y in range(self.height):
            fov.append([False] * self.width)

        for i in range(361):
            ax = sin(radians(i))
            ay = cos(radians(i))

            x = player_x
            y = player_y

            for z in range(3):
                x += ax
                y += ay

                if x < 0 or y < 0 or x > self.width or y > self.height:
                    break

                fov[round(y)][round(x)] = True
                self.cells[round(y)][round(x)].already_seen = True

                if not self.cells[round(y)][round(x)].walkable:
                    break

        return fov
