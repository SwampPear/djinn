from argparse import ArgumentParser
import os


class CLI:
    def __init__(self):
        self.parser = self._init_parser()


    def _init_parser(self):
        parser = ArgumentParser(description='Djinn CLI')

        # command
        parser.add_argument(
            'command',
            choices=[
                'new',
                'start',
                'rm'
            ], 
            help='basic command for djinn')

        # project
        parser.add_argument(
            'project',
            help='name of a project'
        )

        # workspace
        parser.add_argument(
            '--workspace', '-w',
            default=os.getcwd(),
            required=False,
            help='workspace dir')

        return parser


    def _new(self, project, workspace):
        print('new')
        print(project)
        print(workspace)


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
        args = self.parser.parse_args()

        command = args.command
        project = args.project
        workspace = args.workspace

        if command == 'new':
            self._new(project, workspace)
        elif command == 'start':
            self._start(project, workspace)
        elif command == 'rm':
            self._rm(project, workspace)
