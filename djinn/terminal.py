from typing import Self
import sys


class STYLE:
    """
    ASCII terminal styles.
    """
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'


class Terminal:
    """
    Handles terminal interaction.

    Params:
        project - name of the working project
    """
    def __init__(self, project: str) -> Self:
        self.project = project
        self.stdin = ''


    """
    Waits for user input
    """
    def poll(self) -> str:
        # prompt
        sys.stdout.write(f'{STYLE.BOLD}Djinn ({self.project}) % {STYLE.END}')

        # input
        _prompt_in = input()

        return _prompt_in
