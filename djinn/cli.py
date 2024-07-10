from argparse import ArgumentParser
import os


class CLI:
    def __init__(self):
        # init parser
        self.parser = ArgumentParser(description='Djinn CLI')

        # init commands
        # command
        self.parser.add_argument(
            'command', 
            choices=[
                'run',
                'new'
            ], 
            default='new',
            help='basic command for djinn')

        # workspace
        self.parser.add_argument(
            '--workspace', '-o',
            default=os.getcwd(),
            required=False,
            help='adds a workspace dir')
        
        # project name
        self.parser.add_argument(
            '--project', '-p',
            required=False,
            help='sets a project name')
        
    def run(self) -> None:
        # parse args
        args = self.parser.parse_args()

        command = args.command
        workspace = args.workspace
        project = args.project

        if command == 'new':
            # check if project exists
            if not project:
                print('project should be entered')

            
            # create new project dir
            # set settings.json
            print(project)
