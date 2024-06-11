from typing import List


class Style:
    red = '\033[91m'
    green = '\033[92m'
    yellow = '\033[93m'
    cyan = '\033[96m'
    white = '\033[97m'
    end = '\033[0m'
    bold = '\033[1m'


def log(*args: List[str]) -> None:
    output = ''

    for arg in args:
        output += arg

    print(output, end='')
