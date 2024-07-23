import json
import re
from typing import List
from .utils import *


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

        self.workpace = self.init_workspace()
        self.cwd = self.workpace

    """
    Initializes the workspace
    """
    def init_workspace(self) -> str:
        settings_path = f'{DJINN_DIR}/projects/{self.project}/settings.json'

        with open(settings_path, 'r') as file:
            return json.load(file)['workspace']
        

    def parse_instructions(self, instructions: str) -> List[Instruction]:
        parsed = []

        # match specific json
        pattern = r'\{\s*"action":\s*"["a-zA-z0-9:\s_.\\(),=+\']*",\s*"description":\s*"["a-zA-z0-9:\s_.\\(),=\']*"\s*\}'
        matches = re.findall(pattern, instructions, re.DOTALL)

        # build list
        for match in matches:
            parsed.append(json.loads(match))

        return parsed
    

    def execute_instructions(self, instructions: str) -> None:
        parsed_instructions = self.parse_instructions(instructions)

        for instruction in parsed_instructions:
            self.execute_instruction(instruction)

    
    def execute_instruction(self, instruction: Instruction) -> None:
        print(instruction)

