from screen import create_screen
from dungeon import Dungeon
from player import Player


class Game:
    def __init__(self):
        self.screen = create_screen()

        self.dungeon = Dungeon(80, 20)
        self.dungeon.generate()

        self.player = Player(*self.dungeon.random_pos())

    def play(self):
        self.screen.get_key()
        self.screen.draw_dungeon(self.dungeon, self.player)
        self.screen.push_message('Welcome to Necronomicon, my first roguelike...')

        while True:
            char = self.screen.get_key()

            if char == 'q':  # Quit game
                quit = self.screen.ask_message('Do you really want to quit?')
                if quit.lower() in ['y', 'yes']:
                    break

            elif char == '?':  # Show help
                self.screen.push_message('There will be a little help')

            elif char in ['h', 'j', 'k', 'l', 'y', 'u', 'b', 'n']:  # Movement
                success = self.player.move(char, self.dungeon)
                if success:
                    self.screen.draw_dungeon(self.dungeon, self.player)
                    self.screen.update_info(self.player)
                else:
                    self.screen.push_message('You crashed')
