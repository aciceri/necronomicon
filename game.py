from screen import create_screen
from dungeon import Dungeon
from player import Player


class Game:
    def __init__(self):
        self.screen = create_screen()

        self.tmp_dungeon = Dungeon(80, 20)
        self.tmp_dungeon.generate()
        self.dungeons = [self.tmp_dungeon]

        self.player = Player(*self.dungeons[0].up_stair)

    def play(self):
        self.screen.get_key()
        self.screen.draw_dungeon(self.dungeons[self.player.floor - 1], self.player)
        self.screen.push_message('Welcome to Necronomicon, my first roguelike...')

        while True:  # Main game loop
            char = self.screen.get_key()

            if char == 'q':  # Quit game
                quit = self.screen.ask_message('Do you really want to quit?')
                if quit.lower() in ['y', 'yes', 'yea']:
                    break

            elif char == '?':  # Show help
                self.screen.push_message('This is a fantastic game... :)')

            elif char in ['h', 'j', 'k', 'l', 'y', 'u', 'b', 'n', '.']:  # Movement
                success = self.player.move(char, self.dungeons[self.player.floor - 1])
                if success:
                    self.screen.draw_dungeon(self.dungeons[self.player.floor - 1], self.player)
                    self.screen.update_info(self.player)
                else:
                    self.screen.push_message('You can\'t go on this way')

            elif char == '>':
                if self.dungeons[self.player.floor - 1].cell(self.player.x, self.player.y).char == '>':
                    self.dungeons.append(Dungeon(80, 20))
                    self.player.floor += 1
                    self.dungeons[self.player.floor - 1].generate()
                    self.player.moves += 1
                    self.screen.update_info(self.player)
                    self.player.x, self.player.y = self.dungeons[self.player.floor - 1].up_stair
                    self.screen.draw_dungeon(self.dungeons[self.player.floor - 1], self.player)
                    self.screen.push_message('Welcome to the %d floor' % self.player.floor)
                else:
                    self.screen.push_message('There isn\'t down stairs here')

            elif char == '<':
                if self.dungeons[self.player.floor - 1].cell(self.player.x, self.player.y).char == '<':
                    if self.player.floor == 1:
                        self.screen.push_message('You can\'t escape from the dungeon')
                    else:
                        self.player.floor -= 1
                        self.player.moves += 1
                        self.player.x, self.player.y = self.dungeons[self.player.floor - 1].down_stair
                        self.screen.push_message('You returned at the %d dungeon' % self.player.floor)
                        self.screen.update_info(self.player)
                        self.screen.draw_dungeon(self.dungeons[self.player.floor - 1], self.player)
                else:
                    self.screen.push_message('There isn\'up stairs here')
