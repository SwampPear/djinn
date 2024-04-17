import os
import argparse
from pathlib import Path


"""
Performs basic os functions and handles cli input and outpt
"""
class CLI:
    """
    Processes and routes a command based on args.
    """
    def _process_command(self, cmd):
        # use argparsel
        pass

    """
    Provides a description of each command and their syntax.
    """
    def _help(self):
        _message = """
        Commands:
        mkdir:
         - description: creates a directory
         - usage: mkdir <dir>
        """

    """
    Makes a directory and logs results.
    """
    def _mkdir(self, dir):
        try:
            os.mkdir(dir)
        except OSError:
            print("mkdir error")

    """
    Removes a directory and logs results.
    """
    def _rmdir(self, dir):
        try:
            os.rmdir(dir)
        except OSError:
            print("rmdir error")

    """
    Lists the contents of a the current directory and logs results.
    """
    def _ls(self):
        pass

    """
    Lists the contents of a the current directory and all nested directories and 
    logs results.
    """
    def _ls_nested(self):
        pass

    """
    Changes the directory and logs results.
    """
    def _cd(self, cwd, path):
        path = Path(cwd, path)

        os.chdir(path)
        