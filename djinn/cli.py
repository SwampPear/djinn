from argparse import ArgumentParser
import os
import json


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
        dirs = os.listdir('/var/db/Djinn/projects')

        if project in dirs:
            print('project name already taken')
        else:
            # init project dir
            os.mkdir(f'/var/db/Djinn/projects/{project}')
            
            # init data
            with open(f'/var/db/Djinn/projects/{project}/data', 'w') as file:
                file.write('')

            # init project settings
            with open(f'/var/db/Djinn/projects/{project}/settings.json', 'w') as file:
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
        args = self.parser.parse_args()

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
