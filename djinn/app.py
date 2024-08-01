from .cmd import CMD
from .db import Database
from .model import Model
from .settings import DJINN_DIR


class State:
    """
    App state.
    """
    IDLE = 0
    RUNNING = 1
    STOP = 2


class Action:
    """
    Action parsed from llm output.
    """
    action: str
    description: str


class App:
    """
    Interactive djinn app.

    Params:
        project - the working project
        prompt - a prompt
    """
    def __init__(self, project: str, prompt: str):
        self.project = project
        self.prompt = prompt
        self.db = Database(f'{DJINN_DIR}/projects/{self.project}/data')
        self.cmd = CMD(self.project)
        self.model = Model(self.cmd.workspace)

        self.state = State.STOP


    """
    Runns the Djinn app.
    """
    def run(self) -> None:
        query_result = self.model.query(self.prompt)
        print(query_result)
        
        self.cmd.execute_instructions(query_result)
