import os
from argparse import ArgumentParser
import json
from .utils import DJINN_DIR


class CLI:
    """
    Handles startup command and shell interaction.
    """
    def __init__(self):
        self.arg_parser = self._init_parser()


    """
    Initializes the argument parser for terminal command.
    """
    def _init_parser(self) -> ArgumentParser:
        arg_parser = ArgumentParser(description='Djinn CLI')

        arg_parser.add_argument('command', choices=['new', 'start', 'rm'])
        arg_parser.add_argument('project')
        arg_parser.add_argument(
            '--workspace', '-w',
            default=os.getcwd(),
            required=False)

        return arg_parser


    """
    Creates a new Djinn project.

    Params:
        project - name of project
        workspace - workspace directory
    """
    def _new(self, project: str, workspace: str) -> None:
        dirs = os.listdir(f'{DJINN_DIR}/projects')

        if project in dirs:
            print('project name already taken')
        else:
            # init project dir
            os.mkdir(f'{DJINN_DIR}/projects/{project}')
            
            # init data
            with open(f'{DJINN_DIR}/projects/{project}/data', 'w') as file:
                file.write('')

            # init project settings
            with open(f'{DJINN_DIR}/projects/{project}/settings.json', 'w') as file:
                contents = {
                    "project": project,
                    "workspace": workspace
                }

                json.dump(contents, file)


    def _start(self, project, workspace):
        print('start')
        print(project)
        print(workspace)


    def _rm(self, project, workspace):
        print('rm')
        print(project)
        print(workspace)
        
        
    def run(self) -> None:
        # parse args
        args = self.arg_parser.parse_args()

        command = args.command
        project = args.project
        workspace = args.workspace
        project = args.project

        if command == 'new':
            self._new(project, workspace)
        elif command == 'start':
            self._start(project, workspace)
        elif command == 'rm':
            self._rm(project, workspace)
