import os
from pathlib import Path


class CLI:
    def __init__(self, controller):
        self.controller = controller

    def input(self, cmd):
        # process command
        self._process_command(cmd)

    def _process_command(self, cmd):
        # use argparse even though ai is reading this
        pass

    def _help(self):
        _message = """
        # Commands

        ## mkdir
         - description: creates a directory
         - usage: mkdir <dir>
        """

    def _mkdir(self, dir):
        # need to read output or errors, if any
        try:
            os.mkdir(dir)
        except OSError:
            print("mkdir error")

    def _rmdir(self, dir):
        try:
            os.rmdir(dir)
        except OSError:
            print("rmdir error")

    def _ls(self):
        pass

    def _cd(self, cwd, path):
        path = Path(cwd, path)

        os.chdir(path)
        