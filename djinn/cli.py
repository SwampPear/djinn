import json
import os
import shutil
from argparse import ArgumentParser

from .app import App
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

            # startup shell
            self._start(project)


    """
    Starts up a djinn app.

    Params:
        project - name of project
    """
    def _start(self, project: str) -> None:
        dirs = os.listdir(f'{DJINN_DIR}/projects')

        if project not in dirs:
            print('project not found')
        else:
            app = App(project)
            app.run()


    """
    Removes a djinn project.

    Params:
        project - name of project
    """
    def _rm(self, project: str) -> None:
        dirs = os.listdir(f'{DJINN_DIR}/projects')

        if project not in dirs:
            print('project not found')
        else:
            shutil.rmtree(f'{DJINN_DIR}/projects/{project}')
        
    
    """
    Runs the djinn cli.
    """
    def run(self) -> None:
        args = self.arg_parser.parse_args()

        # route commands
        if args.command == 'new':
            self._new(args.project, args.workspace)
        elif args.command == 'start':
            self._start(args.project)
        elif args.command == 'rm':
            self._rm(args.project)
