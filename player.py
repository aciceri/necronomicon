class Player:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.moves = 0
        self.inventory = []

    def move(self, char, dungeon):
        move_x, move_y = 0, 0

        if char == 'h':
            move_x = -1
        elif char == 'j':
            move_y = 1
        elif char == 'k':
            move_y = -1
        elif char == 'l':
            move_x = 1
        elif char == 'y':
            move_x = -1
            move_y = -1
        elif char == 'u':
            move_x = 1
            move_y = -1
        elif char == 'b':
            move_x = -1
            move_y = 1
        elif char == 'n':
            move_x = 1
            move_y = 1

        if dungeon.cells[self.y + move_y][self.x + move_x].walkable:
            self.x += move_x
            self.y += move_y
            self.moves += 1
            return True  # If the movement is possible

        return False  # If the movement is impossible
