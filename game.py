from screen import create_screen
from map import Map


class Game:
    def __init__(self):
        self.screen = create_screen()
        self.m = Map()

        self.screen.get_key()
        self.screen.push_message('ciao')
        self.screen.draw_map(self.m)
        self.screen.get_key()

        while True:
            #char = self.screen.get_key()
            #if not char:
            #    continue
            #if char == 'q':
            #    break
            char = 'c'
            self.screen.push_message('You pressed "%s"' % char)

    def play(self):
        pass
