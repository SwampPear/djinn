import os


DJINN_DIR = f'{os.path.expanduser("~")}/Library/Application Support/Djinn'


"""
Reads content from a file.

Params:
    path - path of file

Return:
    contents of file
"""
def read_file(path: str) -> str:
    with open(path, 'r') as file:
        return file.read()