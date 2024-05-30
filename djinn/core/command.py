from typing import List
import os


"""
Parses and executes a given command.

Params:
    cmd - the command to parse

Returns:
    output of the executed command
"""
def cmd(cmd: str) -> str:
    pass


"""
Returns a description of available commands.

Returns:
    description of available commands
"""
def help() -> str:
    return ''


"""
Creates a directory.

Params:
    args - arguments for the command

Returns:
    output of the function
"""
def mkdir(args: List[str]) -> str:
    # path TODO: relative path
    path = args[0]

    os.mkdir(path)

    # get stdout


"""
Creates a file.

Params:
    args - arguments for the command

Returns:
    output of the function
"""
def touch(args: List[str]) -> str:
    pass


"""
Writes to a file.

Params:
    args - arguments for the command

Returns:
    output of the function
"""
def write(args: List[str]) -> str:
    pass


"""
Reads from a file.

Params:
    args - arguments for the command

Returns:
    output of the function, including the contents of the file
"""
def read(args: List[str]) -> str:
    pass


"""
Lists the contents of a directory.

Params:
    args - arguments for the command

Returns:
    output of the function
"""
def list(args: List[str]) -> str:
    pass
