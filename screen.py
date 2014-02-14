import curses


class Screen:
    def __init__(self, stdscr):
        '''Initialize the screen and check requirements'''
        self.stdscr = stdscr

        if self.stdscr.getmaxyx() < (24, 80):
            raise Exception('This terminal is too small: x > 79 and y > 23')

        curses.curs_set(0)  # Cursor is invisible
        self.stdscr.timeout(50)

        self.win_map = curses.newwin(20, 80, 0, 0)  # Map window
        self.win_msg = curses.newwin(4, 60, 20, 0)  # Message window
        self.win_info = curses.newwin(4, 20, 20, 61)  # General info window

        self.msg_list = []  # Queue for messages

    def push_message(self, message):
        self.msg_list.append(str(message))  # Add new message to queue
        if len(self.msg_list) > 4:  # Manage the list as a queue
            self.msg_list.pop(0)

        self.win_msg.clear()

        for n, msg in enumerate(self.msg_list[::-1]):
            if n == 0:  # If it is the last message
                self.win_msg.addstr(3 - n, 0, msg, curses.A_BOLD)
            else:
                self.win_msg.addstr(3 - n, 0, msg)

        self.win_msg.refresh()  # Auto refresh if a message is added

    def update_info(self):
        '''Update general information'''
        pass

    def draw_dungeon(self, dungeon):
        '''Draw the map'''
        self.win_map.clear()

        # Last character, historical reason
        self.win_map.addch(19, 78, str(dungeon.cell(79, 19)))
        self.win_map.insch(19, 78, ' ')

        for y in range(dungeon.height):
            for x in range(dungeon.width):
                # Except the last character
                if y != 19 or x != 79:
                    self.win_map.addch(y, x, str(dungeon.cell(x, y)))

        self.win_map.refresh()

    def get_key(self):
        '''Return the pressed key'''
        key = self.stdscr.getch()
        curses.noecho()
        if key == 10:
            return ''  # No key pressed
        elif 32 <= key < 127:
            return chr(key)  # ASCII key pressed
        else:
            return None

    def __del__(self):
        '''Exit from curses mode'''
        curses.endwin()


def create_screen():
    '''Return the wrapped screen'''
    return curses.wrapper(Screen)
