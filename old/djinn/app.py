
import json
from .cmd import CMD
from .db import Database
from .model import Model
from .settings import DJINN_DIR


class State:
    IDLE = 0
    RUNNING = 1
    STOP = 2


class Action:
    action: str
    description: str


class App:
    def __init__(self, project: str, prompt: str):
        self.project = project
        self.path = f'{DJINN_DIR}/projects/{self.project}'
        self.workspace = self._init_workspace()

        self.db = Database(self.path)
        self.cmd = CMD(self.project, self.workspace)
        self.model = Model(self.workspace)

        self.prompt = prompt  # TODO: make dynamic

        self.state = State.STOP

    def _init_workspace(self) -> str:
        with open(f'{self.path}/settings.json', 'r') as file:
            return json.load(file)['workspace']


    def run(self) -> None:
        # TODO: make dynamic and iterative
        query_result = self.model.query(self.prompt)

        print(query_result)

        self.cmd.execute_instructions(query_result)