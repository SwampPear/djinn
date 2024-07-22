import json
import os
import shutil
from argparse import ArgumentParser

from .app import App
from .terminal import log, text, STYLE
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
        parser = ArgumentParser(description='Djinn CLI')

        subparsers = parser.add_subparsers(dest='command')

        new_parser = subparsers.add_parser('new', help='creates new project')
        new_parser.add_argument('project', help='name of a project')
        new_parser.add_argument(
            '--workspace',
            '-w',
            required=False,
            default=os.getcwd(),
            help='Print debug info'
        )

        rm_parser = subparsers.add_parser('rm', help='removes a project')
        rm_parser.add_argument('project', help='name of a project')

        prompt_parser = subparsers.add_parser('prompt', 
            help='prompts a project')
        prompt_parser.add_argument('project', help='name of a project')
        prompt_parser.add_argument('prompt', nargs='*', help='prompt')

        return parser


    """
    Creates a new Djinn project.

    Params:
        project - name of project
        workspace - workspace directory
    """
    def _new(self, project: str, workspace: str) -> None:
        dirs = os.listdir(f'{DJINN_DIR}/projects')

        if project in dirs:
            log(text(f'{project} is already a project name\n', 
                [STYLE.RED, STYLE.BOLD]))
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

            log(text(f'{project} successfully created\n', 
                [STYLE.GREEN, STYLE.BOLD]))


    """
    Prompts a djinn app.

    Params:
        project - name of project
    """
    def _prompt(self, project: str, prompt: str) -> None:
        dirs = os.listdir(f'{DJINN_DIR}/projects')

        if project not in dirs:
            log(text(f'{project} not found\n', 
                [STYLE.RED, STYLE.BOLD]))
        else:
            app = App(project, prompt)
            app.run()


    """
    Removes a djinn project.

    Params:
        project - name of project
    """
    def _rm(self, project: str) -> None:
        dirs = os.listdir(f'{DJINN_DIR}/projects')

        if project not in dirs:
            log(text(f'{project} not found\n', 
                [STYLE.RED, STYLE.BOLD]))
        else:
            shutil.rmtree(f'{DJINN_DIR}/projects/{project}')

            log(text(f'{project} successfully removed\n', 
                [STYLE.GREEN, STYLE.BOLD]))
        
    
    """
    Runs the djinn cli.
    """
    def run(self) -> None:
        args = self.arg_parser.parse_args()

        # route commands
        if args.command == 'new':
            self._new(args.project, args.workspace)
        elif args.command == 'prompt':
            self._prompt(args.project, ' '.join(args.prompt))
        elif args.command == 'rm':
            self._rm(args.project)
