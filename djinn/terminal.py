import sys


class STYLE:
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'


class Terminal:
    def __init__(self, project):
        self.project = project
        self.stdin = ''


    def poll(self):
        sys.stdout.write(f'{STYLE.BOLD}Djinn ({self.project}) % {STYLE.END}')

        prompt = input()
        print(prompt)
