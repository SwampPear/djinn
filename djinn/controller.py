import subprocess
from .db import Database
from .model import Model
from settings import *
from .prompt import *


class Controller:
    """
    Controlls all processes.
    """
    def __init__(self, prompt) -> None:
        self.prompt = prompt
        self.db = Database(DB)
        self.model = Model()

    """
    Runs the controller.
    """
    def run(self) -> None:
        # TESTING
        print(self.model.query(format_prompt()))

        #self.model.quit()


    """
    Initializes an automated development session.
    """
    def _init(self) -> None:
        # feed prompt into llm
        # take ouput and feed into aterm (automated terminal)
        output = 'ls'
        self._cmd(output)

        # take output from aterm feed into llm
        # repeat
        pass

    """
    Parses and executes a given command.

    Params:
        cmd - the command to parse

    Returns:
        output of the executed command
    """
    def _cmd(self, cmd: str) -> str:
        # Execute the command
        process = subprocess.Popen(
            cmd, 
            shell=True, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE
        )

        # Get the output and error (if any)
        out, err = process.communicate()

        # Decode bytes to string (assuming utf-8 encoding)
        output_str = out.decode('utf-8')
        error_str = err.decode('utf-8')

        # Print the output and error
        print("Output:", output_str)
        print("Error:", error_str)