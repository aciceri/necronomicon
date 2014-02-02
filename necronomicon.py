#!/usr/bin/env python3
from argparse import ArgumentParser
from game import Game


def main():
    parser = ArgumentParser(
        prog='Necronomicon',
        description='''A coffebreak roguelike game written in Python,
            it is insipired by Sam Raimi\'s "The Evil Dead" series''',
    )
    parser.add_argument(
        '-v', '--version',
        action='version',
        version='0.1'
    )
    args = parser.parse_args()

    game = Game()  # It is run only if no args are passed
    game.play()

if __name__ == '__main__':
    main()
