import re
import json
import argparse
import subprocess
from .log import log, Style
from settings import *



class Action:
    """
    Action parsed from llm output.
    """
    action: str
    description: str


class CMD:
    """
    Controls program logic and handles all processes.
    """
    def __init__(self):
        self.parser = self._init_parser()
        self.cwd = os.getcwd()
        self.stopped = False
        self.tab_size = 4

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

        # communicate to pipe
        out, err = process.communicate()

        # digest output
        out_msg = out.decode('utf-8')
        err_msg = err.decode('utf-8')

        if err_msg != '':
            return err_msg
        
        return out_msg


    """
    Parses instructions from query results.

    Params:
        instructions - string detailing json formatted instructions

    Returns:
        list of parsed instructions
    """
    def _parse_instructions(self, instructions: str) -> List[Action]:
        parsed = []

        # match specific json
        pattern = r'[\{\[]\s*"action":\s*"[^"]+",\s*"description":\s*"[^"]+"\s*[\}\]]'
        matches = re.findall(pattern, instructions, re.DOTALL)

        # build list
        for match in matches:
            parsed.append(json.loads(match))

        return parsed
            

    """
    Executes the instructions from query results.

    Params:
        query_result - result of the query with encoded instructions
    """
    def execute_instructions(self, query_result: str) -> None:
        # parse and execute instructions
        parsed_instructions = self._parse_instructions(query_result)

        for instruction in parsed_instructions:
            self._execute_instruction(instruction['action'])

    
    """
    Executes an individual instruction

    Params:
        instruction - instruction to execute
    """
    def _execute_instruction(self, instruction: str) -> None:
        # parse and route args
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
        elif args.command == 'write':
            self._write(args)
        else:
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

        # TODO: fix write
        # write
        write_parser = subparsers.add_parser('write')
        write_parser.add_argument('start', type=str)
        write_parser.add_argument('end', type=str)
        write_parser.add_argument('path', type=str)
        write_parser.add_argument('contents',  nargs='*')
    
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
    Lists file system objects.
    """
    def _ls(self, args):
        # TODO: implement
        cmd = f'mkdir {self._path(args.path)}'

        log(Style.green, Style.bold, '[cmd]', Style.end, ' ', cmd, '\n')

        self._cmd(cmd)

    """
    Writes to a file.
    """
    def _write(self, args):
        # row, col
        start = [i for i in args.start.split('-')]
        end = [i for i in args.end.split('-')]
        contents = ' '.join(args.contents)
        path = self._path(args.path)

        print(contents)

        #log(Style.green, Style.bold, '[cmd]', Style.end, ' ', cmd, '\n')

        #self._cmd(cmd)

    
    """
    Formats the correct path.
    """
    def _path(self, path: str) -> str:
        # TODO: implement path sanitizing
        return f'{ROOT}/{path}'
    

    """
    Edits a file.
    """
    def _edit_file(self, contents, path, replace=None):
        # TODO: replace with write
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

