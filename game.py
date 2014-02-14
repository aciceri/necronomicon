from screen import create_screen
from dungeon import Dungeon


class Game:
    def __init__(self):
        self.screen = create_screen()
        self.screen.push_message('Welcome to Necronomicon')

        self.dungeon = Dungeon(80, 20)
        self.dungeon.generate(4)

    def play(self):
        while True:
            char = self.screen.get_key()
            if not char:
                continue
            if char == 'q':
                break
            if char == 'd':
                self.screen.push_message('Dungeon updated')
                self.screen.draw_dungeon(self.dungeon)
