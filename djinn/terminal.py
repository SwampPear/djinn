from typing import Self, List
import sys
import pyinputplus as pyip


"""
Formats text with ASCII styling.
"""
def fmt(txt: str, style: List[str] = []) -> str:
    return f"{''.join(style)}{txt}{S.END}"


"""
Logs text to terminal.
"""
def log(txt: str) -> None:
    sys.stdout.write(txt)


class S:
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
    """
    def __init__(self, project: str) -> Self:
        self.project = project
        self.stdin = ''


    """
    Waits for user input
    """
    def prompt(self) -> str:
        name = input()
        
        return name
