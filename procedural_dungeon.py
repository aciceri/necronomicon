from random import randrange


class Room:
    def __init__(self, dungeon):
        max_width, min_width = 14, 5
        max_height, min_height = 6, 4

        invalid = True
        while invalid:
            invalid = False
            self.middle_x = randrange(max_width // 2, dungeon.width - (max_width // 2))
            self.middle_y = randrange(max_height // 2, dungeon.height - (max_height // 2))
            for x in range(self.middle_x - (max_width // 2), self.middle_x + (max_width // 2)):
                for y in range(self.middle_y - (max_height // 2), self.middle_y + (max_height // 2)):
                    if dungeon.cells[y][x]:
                        invalid = True


        invalid = True
        while invalid:
            invalid = False

            self.middle_x = randrange(max_width // 2 + 1, dungeon.width - (max_width // 2 + 1))
            self.middle_y = randrange(max_height // 2 + 1, dungeon.height - (max_height // 2 + 1))

            self.width = randrange(min_width, max_width)
            self.height = randrange(min_height, max_height)
            self.start_x = self.middle_x - (self.width // 2)
            self.start_y = self.middle_y - (self.height // 2)
            self.end_x = self.middle_x + (self.width // 2)
            self.end_y = self.middle_y + (self.height // 2)

            for x in range(self.start_x - 1, self.end_x + 1):
                for y in range(self.start_y - 1, self.end_y + 1):
                    if dungeon.cells[y][x]:
                        invalid = True


class ProceduralDungeon:
    def __init__(self, width, height):
        self.width, self.height = width, height
        self.cells = []
        for y in range(self.height):
            self.cells.append([False for x in range(width)])

    def generate(self, rooms):
        self.rooms = []
        for i in range(rooms):
            room = Room(self)
            self.rooms.append(room)
            for x in range(room.start_x, room.end_x):
                for y in range(room.start_y, room.end_y):
                    self.cells[y][x] = True

        for i in range(rooms - 1):
            room_a = self.rooms[i]
            room_b = self.rooms[i + 1]

            x, y = room_a.middle_x, room_a.middle_y

            while not (x == room_b.middle_x and y == room_b.middle_y):
                if y < room_b.middle_y:
                    y += 1
                elif y > room_b.middle_y:
                    y -= 1
                elif x < room_b.middle_x:
                    x += 1
                elif x > room_b.middle_x:
                    x -= 1

                self.cells[y][x] = True
