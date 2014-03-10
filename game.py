from screen import create_screen
from dungeon import Dungeon
from player import Player


class Game:
    def __init__(self):
        self.screen = create_screen()

        self.dungeon = Dungeon(80, 20)
        self.dungeon.generate()

        self.player = Player(*self.dungeon.up_stair)

    def play(self):
        self.screen.get_key()
        self.screen.draw_dungeon(self.dungeon, self.player)
        self.screen.push_message('Welcome to Necronomicon, my first roguelike...')

        while True:  # Main game loop
            char = self.screen.get_key()

            if char == 'q':  # Quit game
                quit = self.screen.ask_message('Do you really want to quit?')
                if quit.lower() in ['y', 'yes', 'yea']:
                    break

            elif char == '?':  # Show help
                self.screen.push_message('There will be a little help')

            elif char in ['h', 'j', 'k', 'l', 'y', 'u', 'b', 'n', '.']:  # Movement
                success = self.player.move(char, self.dungeon)
                if success:
                    self.screen.draw_dungeon(self.dungeon, self.player)
                    self.screen.update_info(self.player)
                else:
                    self.screen.push_message('You bump something')

            elif char == '>':
                if self.dungeon.cell(self.player.x, self.player.y).char == '>':
                    self.dungeon.generate()
                    self.player.floor += 1
                    self.player.moves += 1
                    self.screen.update_info(self.player)
                    self.player.x, self.player.y = self.dungeon.up_stair
                    self.screen.draw_dungeon(self.dungeon, self.player)
                    self.screen.push_message('Welcome to the %d floor' % self.player.floor)
                else:
                    self.screen.push_message('There is not stair here')

            elif char == '<':
                if self.dungeon.cell(self.player.x, self.player.y).char == '<':
                    self.screen.push_message('This feature is not implemented yet')
                else:
                    self.screen.push_message('There is no stair here')
