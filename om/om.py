from enum import Enum
from cli import CLI
from utils import config

State = Enum('State', ['START', 'RUN', 'STOP'])

class Om:
    def __init__(self):
        self.root = config('root')
        self.cwd = self.root

        self.cli = CLI()

        self.state = State.START
        self.exit = False

    def run(self):
        while not self.exit:
            if self.state == State.START:
                pass
            elif self.state == State.RUN:
                pass
            elif self.state == State.STOP:
                pass