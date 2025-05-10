import json
import re
import os
from typing import List
from .settings import *


class Instruction:
    action: str
    description: str


class CMD:
    def __init__(self, path: str, workspace: str) -> None:
        self.path = path
        self.workspace = workspace
        self.cwd = self.workspace
        

    def parse_instructions(self, instructions: str) -> List[Instruction]:
        parsed = []

        # match json
        pattern = r'\[[a-zA-Z0-9!@#$%^&*()\-_=+|\\\[\]{}:;\"\',.<>?/`~\sé]+\]'
        match = re.findall(pattern, instructions, re.DOTALL)[0]

        for instruction in json.loads(match):
            parsed.append(instruction)

        return parsed
    

    def execute_instructions(self, instructions: str) -> None:
        parsed_instructions = self.parse_instructions(instructions)

        for instruction in parsed_instructions:

            action = instruction['action']
            command = action.split(' ')[0]

            print(action)

            if command == 'write':
                self._write(action)
            else:
                self._execute_cmd(action)

    
    """
    Writes some text to a file.
    """
    def _write(self, action: str) -> None:
        file = action.split(' ')[1]
        content = ' '.join(action.split(' ')[2:])[1:-1]
        content = content.replace('\\n', '\n')
        content = content.replace('\\\"', '"')

        with open(file, 'w') as f:
            print((file, content))
            f.write(content)


    """
    Executes a terminal instruction.
    """
    def _execute_cmd(self, action: str) -> None:
        os.system(action)
