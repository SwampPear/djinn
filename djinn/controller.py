import subprocess
import re
import json
import argparse
from typing import List
from .db import Database
from .model import Model
from .log import log, Style
from settings import *


class State:
    """
    State of the controller.
    """
    RUNNING = 0     # already running
    START   = 1     # initially starting
    STOP    = 2     # initially stopping


class Action:
    """
    Action parsed from llm output.
    """
    action: str
    description: str


class Controller:
    """
    Controls program logic and handles all processes.
    """
    def __init__(self):
        self.db = Database(DB_PATH)
        self.model = Model()

        self.parser = self._init_parser()
        self.cwd = os.getcwd()
        self.stopped = False
        self.tab_size = 4


    """
    Main execution loop for this controller.
    """
    def run(self) -> None:
        state = State.START

        while not self.stopped:
            if state == State.START:
                # buildup
                state = State.RUNNING

            elif state == State.RUNNING:
                # 1. begin with prompt
                prompt = 'write a program that implements a function in python that multiplies two numbers'

                # query model with (formatted) prompt
                log(Style.cyan, Style.bold, '[prompt]', Style.end, ' ', prompt, '\n')

                result = self.model.query(prompt)

                # iterate over and execute actions, feed output back into model
                self._execute_instructions(result)

                # 4. evaluate effectiveness of actions AFTER ALL ACTIONS COMPLETED
                # 5. repeat 2-4 until effectiveness sufficient
                # 6. repeat 1-5 until process terminated 

                state = State.STOP

            elif state == State.STOP:       # on initial stop
                # teardown
                self._quit()
                self.stopped = True

            else:
                pass


    """
    Terminates all processes.
    """
    def _quit(self) -> None:
        self.model.quit()
        self.stopped = True

    """
    Executes a given command.

    Params:
        cmd - the command to execute

    Returns:
        error if error present, otherwise output
    """
    def _cmd(self, cmd: str) -> str:
        # execute command
        process = subprocess.Popen(
            cmd, 
            shell=True, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE
        )

        out, err = process.communicate()

        output_str = out.decode('utf-8')
        error_str = err.decode('utf-8')

        if error_str != '':
            return error_str
        
        return output_str


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
        # parse instructions
        parsed_instructions = []

        pattern = r'[\{\[]\s*"action":\s*"[^"]+",\s*"description":\s*"[^"]+"\s*[\}\]]'
        matches = re.findall(pattern, query_result, re.DOTALL)

        for match in matches:
            parsed_instructions.append(json.loads(match))

        # execute parsed instructions
        for instruction in parsed_instructions:
            self._execute_instruction(instruction['action'])

    
    """
    Executes an individual instruction

    Params:
        instruction - the instruction to execute
    """
    def _execute_instruction(self, instruction: str) -> None:
        args = self.parser.parse_args(instruction.split())

        if args.command == 'cd':
            self._cd(args)
        elif args.command == 'chmod':
            pass
        elif args.command == 'touch':
            self._touch(args)
        elif args.command == 'mkdir':
            self._mkdir(args)
        elif args.command == 'echo':
            self._echo(args)
            pass


    """
    Initializes an argument parser.

    Returns:
        the argument parser
    """
    def _init_parser(self) -> argparse.ArgumentParser:
        parser = argparse.ArgumentParser(description='instructions')
        subparsers = parser.add_subparsers(dest='command')

        # mkdir
        mkdir_parser = subparsers.add_parser('mkdir')
        mkdir_parser.add_argument('path', type=str)

        # touch
        touch_parser = subparsers.add_parser('touch')
        touch_parser.add_argument('path', type=str)

        # cd
        cd_parser = subparsers.add_parser('cd')
        cd_parser.add_argument('path', type=str)

        # echo
        echo_parser = subparsers.add_parser('echo')
        echo_parser.add_argument('options', nargs='*')
        
        # chmod
        chmod_parser = subparsers.add_parser('chmod')
        chmod_parser.add_argument('permissions', type=str)
        chmod_parser.add_argument('path', type=str)
    
        return parser
    

    """
    Changes the cwd.
    """
    def _cd(self, args):
        self.cwd = f'{self.cwd}/{args.path}'
        print(self.cwd)

        log(Style.green, Style.bold, '[cmd]', Style.end, ' ', self.cwd, '\n')

    """
    Changes the permissions of a file.
    """
    def _chmod(self):
        # TODO: imeplement
        pass


    """
    Creates a new file.
    """
    def _touch(self, args):
        cmd = f'touch {self._path(args.path)}'

        log(Style.green, Style.bold, '[cmd]', Style.end, ' ', cmd, '\n')

        self._cmd(cmd)


    """
    Creates a directory.
    """
    def _mkdir(self, args):
        cmd = f'mkdir {self._path(args.path)}'

        log(Style.green, Style.bold, '[cmd]', Style.end, ' ', cmd, '\n')

        self._cmd(cmd)


    """
    Echoes to terminal.
    """
    def _echo(self, args):
        contents = args.options[0:len(args.options) - 2]
        path = self._path(args.options[-1])

        cmd = f'echo {" ".join(contents)} >> {path}'

        log(Style.green, Style.bold, '[cmd]', Style.end, ' ', cmd, '\n')

        self._cmd(cmd)

    
    """
    Formats the correct path.
    """
    def _path(self, path: str) -> str:
        return f'{ROOT}/{path}'
    

    """
    Edits a file.
    """
    def _edit_file(self, contents, path, replace=None):
        with open(path, 'w') as file:
            file.write(contents)

        """
        # TODO: implement file buffer
        file_contents = ''

        with open(path, 'r', encoding='utf-8') as file:
            file_contents = file.read()

            if replace:
                x_c, x_r = replace[0]
                y_c, _r = replace[0]
                pass
            else:
                file_contents = contents

        with open(path, 'w') as file:
            file.write(file_contents)
        """

