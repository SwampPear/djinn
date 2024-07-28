import json
import re
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
        pattern = r'\{\s*"action":\s*"["a-zA-z0-9:\s_.\\(),=+\'!#/]*",\s*"description":\s*"["a-zA-z0-9:\s_.\\(),=\'!#/]*"\s*\}'
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
            self.execute_instruction(instruction)

    
    """
    Executes a parsed instruction.
    """
    def execute_instruction(self, instruction: Instruction) -> None:
        action = instruction['action']
        command = action.split(' ')[0]

        if command == 'write':
            self.write(action)
        else:
            self.execute_cmd(action)

    
    """
    Writes some text to a file.
    """
    def write(self, action: str) -> None:
        file, content = self.parse_write_action(action)
        print((file, content))

    
    """
    Parses content from from a write action.
    """
    def parse_write_action(self, action: str) -> tuple:
        file = action.split(' ')[1]
        content = ' '.join(action.split(' ')[2:])[1:-1]

        return (file, content)


    """
    Executes a terminal instruction.
    """
    def execute_cmd(self, action: str) -> None:
        print(action)

