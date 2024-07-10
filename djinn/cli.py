from argparse import ArgumentParser, Namespace
import os


class CLI:
    def __init__(self):
        # init parser
        self.parser = ArgumentParser(description='Djinn CLI')

        # init commands
        # command
        self.parser.add_argument('command',
            help='basic command for djinn')

        # workspace
        self.parser.add_argument('--workspace', '-o', default=os.getcwd(),
            help='adds a workspace dir')
        
    def run(self) -> None:
        args = self.parser.parse_args()
