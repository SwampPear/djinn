import json
import re
import os
from typing import List
from .settings import *


class Instruction:
    """
    Instruction parsed from llm output.
    """
    action: str
    description: str


class CMD:
    """
    Controls terminal command interface.
    """
    def __init__(self, project: str) -> None:
        self.project = project

        self.workspace = self.init_workspace()
        self.cwd = self.workspace

    """
    Initializes the workspace
    """
    def init_workspace(self) -> str:
        settings_path = f'{DJINN_DIR}/projects/{self.project}/settings.json'

        with open(settings_path, 'r') as file:
            return json.load(file)['workspace']
        

    """
    Parses json instructions from natural language.
    """
    def parse_instructions(self, instructions: str) -> List[Instruction]:
        parsed = []

        # match specific json
        pattern = '\{\s*"action":\s*"[a-zA-z0-9!@#$%^&*()\-_=+|\\\[\]{}:;\"\',.<>?/`~\s]*",\s*"description":\s*"[a-zA-z0-9!@#$%^&*()\-_=+|\\\[\]{}:;\"\',.<>?/`~\s]*"\s*\}'
        matches = re.findall(pattern, instructions, re.DOTALL)

        # build list
        for match in matches:
            parsed.append(json.loads(match))

        return parsed
    

    """
    Executes parsed instructions.
    """
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

        with open(file, 'w') as f:
            print((file, content))
            f.write(content)


    """
    Executes a terminal instruction.
    """
    def _execute_cmd(self, action: str) -> None:
        os.system(action)
