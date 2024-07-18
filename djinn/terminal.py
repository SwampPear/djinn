from typing import Self, List
import sys


"""
Formats text with ASCII styling.

Params:
    txt - text to format
    style - styles to apply
"""
def text(txt: str, style: List[str] = []) -> str:
    return f"{''.join(style)}{txt}{STYLE.END}"


"""
Writes some text to the terminal.

Params:
    txt - text to write
"""
def log(txt: str) -> None:
    sys.stdout.write(txt)


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
    def prompt(self) -> str:
        prompt = input(text(f'Djinn ({self.project}) % ', [STYLE.BOLD]))

        return prompt
