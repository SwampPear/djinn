import json
import os
import shutil
from argparse import ArgumentParser
from .app import App
from .terminal import log, fmt, S
from .settings import DJINN_DIR


class CLI:
    """
    Handles Djinn command line interface.
    """
    def __init__(self):
        self.arg_parser = self._init_parser()


    """
    Initializes the argument parser for terminal command.
    """
    def _init_parser(self) -> ArgumentParser:
        parser = ArgumentParser(description='Djinn CLI')
        subparsers = parser.add_subparsers(dest='command')

        # new
        new_parser = subparsers.add_parser('new', help='creates new project')
        new_parser.add_argument('project', help='name of a project')
        new_parser.add_argument(
            '--workspace',
            '-w',
            required=False,
            default=os.getcwd(),
            help='Print debug info'
        )

        # rm
        rm_parser = subparsers.add_parser('rm', help='removes a project')
        rm_parser.add_argument('project', help='name of a project')

        # prompt
        prompt_parser = subparsers.add_parser('prompt', 
            help='prompts a project')
        prompt_parser.add_argument('project', help='name of a project')
        prompt_parser.add_argument('prompt', nargs='*', help='prompt')

        return parser


    """
    Creates a new Djinn project.
    """
    def _new(self, project: str, workspace: str) -> None:
        dirs = os.listdir(f'{DJINN_DIR}/projects')

        if project in dirs:
            log(fmt(
                f'\'{project}\' is already a project name\n', [S.RED, S.BOLD]))
            
        else:
            # init project data
            project_path = f'{DJINN_DIR}/projects/{project}'

            os.mkdir(project_path)
            
            with open(f'{project_path}/data', 'w') as file:
                file.write('')

            with open(f'{project_path}/settings.json', 'w') as file:
                settings = {
                    "project": project,
                    "workspace": workspace
                }

                json.dump(settings, file)

            log(fmt(f'{project} successfully created\n', [S.GREEN, S.BOLD]))


    """
    Prompts a djinn app.

    Params:
        project - name of project
    """
    def _prompt(self, project: str, prompt: str) -> None:
        dirs = os.listdir(f'{DJINN_DIR}/projects')

        if project not in dirs:
            log(fmt(f'\'{project}\' not found\n', [S.RED, S.BOLD]))

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
            log(fmt(f'\'{project}\' not found\n', [S.RED, S.BOLD]))

        else:
            shutil.rmtree(f'{DJINN_DIR}/projects/{project}')

            log(fmt(f'{project} successfully removed\n', [S.GREEN, S.BOLD]))
        
    
    """
    Runs the djinn cli.
    """
    def run(self) -> None:
        args = self.arg_parser.parse_args()

        if args.command == 'new':
            self._new(args.project, args.workspace)

        elif args.command == 'prompt':
            project = args.project
            prompt = ' '.join(args.prompt)

            self._prompt(args.project, ' '.join(args.prompt))
            
        elif args.command == 'rm':
            self._rm(args.project)
