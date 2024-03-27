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
        # use argparse
        pass

    """
    Provides a descsription of each command and their syntax.
    """
    def _help(self):
        pass

    """
    Makes a directory and logs results.
    """
    def _mkdir(self, dir):
        try:
            os.mkdir(dir)
        except OSError:
            pass

    """
    Removes a directory and logs results.
    """
    def _rmdir(self, dir):
        try:
            os.rmdir(dir)
        except OSError:
            pass

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
        