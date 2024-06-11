import subprocess
import re
import json
from typing import List
from .db import Database
from .model import Model
from settings import *


class State:
    RUNNING = 0
    START   = 1
    STOP    = 2


class Action:
    action: str
    description: str


class Controller:
    """
    Controlls all processes.
    """
    def __init__(self) -> None:
        # modules
        self.db = Database(DB_PATH)
        self.model = Model()

        # state

    """
    Runs the controller.
    """
    def run(self) -> None:
        stop = False
        state = State.START

        while not stop:
            if state == State.START:        # initially starting
                # buildup
                state = State.RUNNING

            elif state == State.RUNNING:    # active state
                # 1. begin with prompt
                prompt = 'write a program that implements a function in python that multiplies two numbers'

                # query model with (formatted) prompt
                result = self.model.query(prompt)

                print(result)
                
                # these should also be local to the controller:

                # 3. iterate over and execute actions, feed output back into model
                self._execute_instructions(result)
                # 4. evaluate effectiveness of actions AFTER ALL ACTIONS COMPLETED
                # 5. repeat 2-4 until effectiveness sufficient
                # 6. repeat 1-5 until process terminated 

                state = State.STOP

            elif state == State.STOP:       # on initial stop
                # teardown
                self._quit()
                stop = True

            else:
                pass

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


    """
    Terminates all processes.
    """
    def _quit(self) -> None:
        self.model.quit()

    """
    Parses instructions from query results.
    """
    def _parse_instructions(self, instructions: str) -> List[Action]:
        parsed = []

        pattern = r'[\{\[]\s*"action":\s*"[^"]+",\s*"description":\s*"[^"]+"\s*[\}\]]'
        matches = re.findall(pattern, instructions, re.DOTALL)

        for match in matches:
            parsed.append(json.loads(match))

        return parsed
            

    """
    Executes the instructions from query results.

    Params:
        query_result - result of the query with encoded instructions
    """
    def _execute_instructions(self, query_result: str) -> None:
        parsed_instructions = self._parse_instructions(query_result)

        for instruction in parsed_instructions:
            self._execute_instruction(instruction)

    
    """
    Executes an individual instruction
    """
    def _execute_instruction(self, instruction: str) -> None:
        # TODO: implement instruction parsing
                
        # regex match instructions
        print(instruction)